FROM squidfunk/mkdocs-material
RUN pip install mkdocs-git-revision-date-localized-plugin
RUN pip install mkdocs-git-authors-plugin
RUN pip install mkdocs-glightbox
RUN pip install mkdocs-macros-plugin
