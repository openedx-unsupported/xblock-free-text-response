## Localization targets

WORKDIR := $(module_root)
I18N_SOURCE_DIR := $(WORKDIR)/translations/en/LC_MESSAGES

translations_rename_to_textmo:  ## Renames django-partial.po to text.mo for XBlock compatibility
	cat $(I18N_SOURCE_DIR)/django-partial.po |  \
	   grep -v 'Plural-Forms: nplurals' > $(I18N_SOURCE_DIR)/text.po
	rm -fv $(I18N_SOURCE_DIR)/django-partial.po

translations_extract: ## extract strings to be translated, outputting .po files
	# Extract Python and Django template strings
	mkdir -p $(I18N_SOURCE_DIR)
	uv run tox -e translations_extract
	make translations_rename_to_textmo

translations_compile: ## compile translation files, outputting .mo files for each supported language
	uv run tox -e translations_compile

translations_detect_changed: ## Determines if the source translation files are up-to-date, otherwise exit with a non-zero code.
	uv run tox -e translations_detect_changed || \
	    (  \
	        echo "====" &&  \
	        echo "Translations have changes. Run 'make translations_extract' locally to update them." &&  \
	        echo "====" &&  \
	        exit 1  \
        )
	make translations_rename_to_textmo

translations_pull: ## pull translations from Transifex
	uv run tox -e translations_pull
	make translations_compile

translations_push: translations_extract ## push source translation files (.po) to Transifex
	uv run tox -e translations_push

translations_dummy: ## generate dummy translation (.po) files
	uv run tox -e translations_dummy

translations_build_dummy: translations_extract translations_dummy translations_compile ## generate and compile dummy translation files

translations_validate: translations_build_dummy translations_detect_changed ## validate translations
