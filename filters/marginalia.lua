local function escape_html(str)
  return (str
    :gsub("&", "&amp;")
    :gsub("<", "&lt;")
    :gsub(">", "&gt;")
    :gsub('"', "&quot;"))
end

local function has_class(el, class)
  for _, c in ipairs(el.classes) do
    if c == class then
      return true
    end
  end
  return false
end

local function render_inlines(inlines)
  local html = pandoc.write(pandoc.Pandoc({ pandoc.Plain(inlines) }), "html")
  return (html:gsub("^%s+", ""):gsub("%s+$", ""))
end

function Div(el)
  if not has_class(el, "commentary") then
    return nil
  end

  local title = el.attributes.title
    or el.attributes["data-title"]
    or el.attributes.label
  local title_html = title and escape_html(title) or nil

  if not title and #el.content > 0 then
    local first = el.content[1]
    if first.t == "Header" then
      title_html = render_inlines(first.content)
      table.remove(el.content, 1)
    elseif first.t == "Para" and #first.content > 0 and first.content[1].t == "Strong" then
      title_html = render_inlines(first.content[1].content)
      local remaining = {}
      for i = 2, #first.content do
        table.insert(remaining, first.content[i])
      end
      if #remaining > 0 and (remaining[1].t == "Space" or remaining[1].t == "SoftBreak" or remaining[1].t == "LineBreak") then
        table.remove(remaining, 1)
      end
      if #remaining > 0 then
        el.content[1] = pandoc.Para(remaining)
      else
        table.remove(el.content, 1)
      end
    end
  end

  title_html = title_html or "Commentary"

  local blocks = pandoc.List()
  blocks:insert(pandoc.RawBlock("html", "<span class=\"commentary-anchor\" aria-hidden=\"true\"></span>"))
  blocks:insert(pandoc.RawBlock("html", "<details class=\"commentary\" data-commentary=\"1\">"))
  blocks:insert(pandoc.RawBlock(
    "html",
    "<summary><span class=\"commentary-toggle\" aria-hidden=\"true\"></span><span class=\"commentary-title\">" .. title_html .. "</span></summary>"
  ))
  blocks:insert(pandoc.RawBlock("html", "<div class=\"commentary-body\">"))
  for _, block in ipairs(el.content) do
    blocks:insert(block)
  end
  blocks:insert(pandoc.RawBlock("html", "</div></details>"))

  return blocks
end
