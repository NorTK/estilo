# GNUmakefile para la Guía de Estilo de Documentación para NorTK
# Compilación y validación de documentación Sphinx

SPHINXOPTS    ?= -W --keep-going
SPHINXBUILD   ?= sphinx-build
AUTOBUILD     ?= sphinx-autobuild
HOST          ?= 127.0.0.1
PORT          ?= 8000
AUTOBUILDOPTS ?= --host $(HOST) --port $(PORT) --watch $(SOURCEDIR) --ignore "$(BUILDDIR)/*" --ignore ".agents/*" --ignore "*.swp" --ignore "*~"
SOURCEDIR     := source
BUILDDIR      := build
RSTCHECK      ?= rstcheck
CRSTLINT      ?= crstlint
WEASYPRINT    ?= weasyprint

.PHONY: all html dirhtml singlehtml latex latexpdf pdf linkcheck lint fix hooks dev clean help

all: html

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

dev: | $(BUILDDIR)
	@echo "Iniciando servidor de desarrollo con sphinx-autobuild (dirhtml)..."
	@echo "Servidor disponible en http://$(HOST):$(PORT)/ (Recarga en vivo activada)"
	@$(AUTOBUILD) -b dirhtml "$(SOURCEDIR)" "$(BUILDDIR)/dirhtml" $(AUTOBUILDOPTS)

html: | $(BUILDDIR)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)
	@echo "Documentación HTML compilada con éxito en $(BUILDDIR)/html"

dirhtml: | $(BUILDDIR)
	@$(SPHINXBUILD) -b dirhtml "$(SOURCEDIR)" "$(BUILDDIR)/dirhtml" $(SPHINXOPTS)

singlehtml: | $(BUILDDIR)
	@$(SPHINXBUILD) -b singlehtml "$(SOURCEDIR)" "$(BUILDDIR)/singlehtml" $(SPHINXOPTS)

latex: | $(BUILDDIR)
	@$(SPHINXBUILD) -b latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" $(SPHINXOPTS)

latexpdf: | $(BUILDDIR)
	@echo "Generando documento PDF completo con Sphinx (latexpdf)..."
	@$(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)
	@cp -f "$(BUILDDIR)/latex/nortk-guia-estilo-v0.1.0.pdf" "$(BUILDDIR)/nortk-guia-estilo-v0.1.0.pdf"
	@echo "Documento PDF generado exitosamente en $(BUILDDIR)/nortk-guia-estilo-v0.1.0.pdf"

pdf: latexpdf

linkcheck: | $(BUILDDIR)
	@$(SPHINXBUILD) -b linkcheck "$(SOURCEDIR)" "$(BUILDDIR)/linkcheck" $(SPHINXOPTS)

lint:
	@echo "Ejecutando rstcheck recursivo en fuentes..."
	@$(RSTCHECK) -r .
	@echo "Verificación rstcheck exitosa."

fix:
	@echo "Ejecutando crstlint para corregir problemas comunes de formato..."
	@$(CRSTLINT) -fr .
	@echo "Corrección automática con crstlint completada."

hooks:
	@git config core.hooksPath .githooks
	@chmod +x .githooks/pre-push
	@echo "Hooks de Git configurados (.githooks/pre-push activo)."

clean:
	@rm -rf "$(BUILDDIR)"
	@echo "Directorio de compilación $(BUILDDIR) eliminado."

$(BUILDDIR):
	@mkdir -p "$@"
