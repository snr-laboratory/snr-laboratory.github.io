# Makefile
PANDOC ?= pandoc

CONTENT_DIR := content
THEME_DIR   := theme
ASSETS_DIR  := assets
OUT_DIR     := docs

MD_SRC      := $(wildcard $(CONTENT_DIR)/*.md)
INDEX_MD    := $(CONTENT_DIR)/index.md
NOTFOUND_MD := $(CONTENT_DIR)/404.md
PAGE_MD     := $(filter-out $(INDEX_MD) $(NOTFOUND_MD), $(MD_SRC))
BUILD_DEPS  := Makefile $(wildcard $(THEME_DIR)/*.html) $(wildcard filters/*.lua)

HTML_OUT := $(OUT_DIR)/index.html \
  $(OUT_DIR)/404.html \
  $(patsubst $(CONTENT_DIR)/%.md,$(OUT_DIR)/%/index.html,$(PAGE_MD))

PANDOC_FLAGS := \
  --from=markdown+fenced_divs+tex_math_dollars+tex_math_single_backslash \
  --to=html5 \
  --standalone \
  --template=$(THEME_DIR)/template.html \
  --include-before-body=$(THEME_DIR)/nav.html \
  --include-after-body=$(THEME_DIR)/footer.html \
  --css=assets/style.css \
  --lua-filter=filters/marginalia.lua \
  --mathjax=https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js \
  --metadata=lang:en \
  --metadata=site-title:"The SNR Laboratory"

.PHONY: build check clean copy-assets rebuild serve

build: copy-assets $(OUT_DIR)/CNAME $(HTML_OUT)

$(OUT_DIR)/CNAME: CNAME | $(OUT_DIR)
	cp CNAME $(OUT_DIR)/CNAME

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

copy-assets: | $(OUT_DIR)
	rm -rf $(OUT_DIR)/assets
	cp -r $(ASSETS_DIR) $(OUT_DIR)/assets

$(OUT_DIR)/index.html: $(INDEX_MD) $(BUILD_DEPS) | $(OUT_DIR)
	$(PANDOC) $(PANDOC_FLAGS) --metadata=pagetitle:Home -o $@ $<

$(OUT_DIR)/404.html: $(NOTFOUND_MD) $(BUILD_DEPS) | $(OUT_DIR)
	$(PANDOC) $(PANDOC_FLAGS) --metadata=pagetitle:404 -o $@ $<

$(OUT_DIR)/%/index.html: $(CONTENT_DIR)/%.md $(BUILD_DEPS) | $(OUT_DIR)
	mkdir -p $(dir $@)
	$(PANDOC) $(PANDOC_FLAGS) --metadata=pagetitle:$* -o $@ $<

check: build
	test -f $(OUT_DIR)/index.html
	test -f $(OUT_DIR)/404.html
	test -f $(OUT_DIR)/CNAME
	cmp -s CNAME $(OUT_DIR)/CNAME
	@echo "Build checks passed."

clean:
	rm -rf $(OUT_DIR)

rebuild:
	$(MAKE) clean
	$(MAKE) build

serve: build
	python3 -m http.server --directory $(OUT_DIR) 8000
