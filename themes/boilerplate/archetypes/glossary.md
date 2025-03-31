+++
title = '{{ replace .File.ContentBaseName "-" " " | title }}'
date = {{ .Date }}
draft = true
url = ""
description = ""
keywords = []
image = ""
term = "{{ replace .File.ContentBaseName "-" " " | title }}"
shortDescription = ""
category = "{{ substr (replace .File.ContentBaseName "-" " " | title) 0 1 | upper }}"
tags = []
faq = [
  {
    question = "What is {{ replace .File.ContentBaseName "-" " " | title }}?",
    answer = ""
  },
  {
    question = "How does {{ replace .File.ContentBaseName "-" " " | title }} work?",
    answer = ""
  }
]
additionalImages = []
+++

Write the long description of the term here. This can include multiple paragraphs, lists, and other markdown formatting.

## Key Points

- First key point about {{ replace .File.ContentBaseName "-" " " | title }}
- Second key point about {{ replace .File.ContentBaseName "-" " " | title }}
- Third key point about {{ replace .File.ContentBaseName "-" " " | title }}
