Feature: Convert markdown files to docx
  In order to work more effectively with git 
  As a writer
  I want to convert markdown files into docx files
  


Scenario: Convert markdown to Pandoc With No Template
Given a input markdown file
When we convert that file through pandoc
Then we have a docx file as output
