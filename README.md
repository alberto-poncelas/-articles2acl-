
# PDF to ACL

This project to build a proceedings from the individual papers (in pdf format) and convert it to [ACL anthology](https://aclweb.org/anthology/) format.
It is divided in two main parts:
1. Building the Proceedings: A Latex project to create the proceedings
2. Conversion to ACL Format: Create a file for ACL anthology containing the pdf, bib files etc.

## Building the Proceedings

The first step is to create the pdf of the proceedings. Use the latex template `latex_template` and edit as follows:

* Edit in `main.tex` the variables (`\proceedingsTitle`,`\conferenceURL`, etc.)
* Add the conference logos in the path `Template/logos/` and edit `Template/Cover` and `Template/Cover2`
* Edit `preface.tex`
* Edit `organizers.tex`
* Add the papers (pdf format) in the `papers` folder.
* In `papers.tex` add `\indexauthors{names}` (names are separated by semi-colon) and `\insertmydocument{Paper Name}{names}{papers/paper_name.pdf}` (names are separated by comma) for each paper.

This makes the proceedings with the papers with the index, author index, and footnotes with the name of the conference and page number.

## Conversion to ACL Format

Place the pdf in the desired folder and add the files `list` and `meta`:

* Create a `list` file where each row contains (tab-separated) the name of the authors, name of the paper and index as follows:
 ```
Name1, Name2	PaperName	1
```
* Create a `meta` file as described in [easy2acl](https://github.com/acl-org/easy2acl).

(you can find and example of these in `example_proceedings`)

* Run the command:

```
bash convert2acl.sh example_proceedings
```

