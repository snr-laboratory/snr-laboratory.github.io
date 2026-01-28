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

function Div(el)
  if not has_class(el, "commentary") then
    return nil
  end

  local title = el.attributes.title
    or el.attributes["data-title"]
    or el.attributes.label

  if not title and #el.content > 0 then
    local first = el.content[1]
    if first.t == "Header" then
      title = pandoc.utils.stringify(first.content)
      table.remove(el.content, 1)
    elseif first.t == "Para" and #first.content > 0 and first.content[1].t == "Strong" then
      title = pandoc.utils.stringify(first.content[1])
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

  title = title or "Commentary"

  local safe_title = escape_html(title)
  local blocks = pandoc.List()
  blocks:insert(pandoc.RawBlock("html", "<details class=\"commentary\" data-commentary=\"1\">"))
  blocks:insert(pandoc.RawBlock(
    "html",
    "<summary><span class=\"commentary-toggle\" aria-hidden=\"true\"></span><span class=\"commentary-title\">" .. safe_title .. "</span></summary>"
  ))
  blocks:insert(pandoc.RawBlock("html", "<div class=\"commentary-body\">"))
  for _, block in ipairs(el.content) do
    blocks:insert(block)
  end
  blocks:insert(pandoc.RawBlock("html", "</div></details>"))

  return blocks
end
