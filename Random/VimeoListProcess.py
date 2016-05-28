import html2text
import os
import codecs
import re

def onlywhite(line):
    """Return true if the line does only consist of whitespace characters."""
    for c in line:
        if c is not ' ' and c is not '  ':
            return c is ' '
    return line

def stripConstantGumf(line):

    fixedTokens = ['[ ![]', '[\+ More details]', '[Watch Later]', '[Upload]', '[Date]' , '[Alphabetical]', '[Alphabetical]','[Plays]', '[Likes]', '[Comments]', '[Customize]', '[s]', '[Duration]' ]

    if re.match("\\*.",line):
        return ""

    if re.match("\d+:\d\d:\d\d",line) or re.match("\d\d:\d\d",line):
        return "[" + line.rstrip() + "]"

    if line.startswith('#'):
        return ""

    if line.startswith('[ ](//vimeo.com)'):
        return ""

    for s in fixedTokens:
        if s in line:
            return ""

    return line

def getUrlFromLine(line):
    # get the first (
    # get the closing  )
    # get whats in between?

    if '(' in line and ')' in line:
        opening = line.index('(')
        closing = line.index(')')
        url = line[opening + 1:closing]

        #print(line, opening, closing, url)
        return url

    return line

def processReadMeIntoDictionary():
    entries = []

    path = 'C:\\Temp\\VimeoList\\readme.md'
    with codecs.open(path, "r",encoding='ascii', errors='ignore') as f:
        for line in f:
            if line.startswith('- ['):
                url = getUrlFromLine(line)
                entries.append(url)
        f.close()

    return entries

def processFilesIntoLinksList():

    links = []

    inLink = False
    currentLine = ""
    path = "c:\\temp\\vimeolist"

    allFiles = os.listdir(path)
    for filename in allFiles:
        if filename.endswith(".new"):
            f = open(filename, 'r')

            for line in f:
                line = line.strip()
                dataline = stripConstantGumf(line).strip('')

                if not onlywhite(dataline):
                    # if not in a commentedout block look for the beginning of a commentedout block
                    if not inLink:
                        if '[ ![]' in dataline:
                            inLink = False
                        elif dataline.startswith('['):
                            inLink = True

                    if inLink and re.match("\[\d+:", dataline):
                        currentLine = currentLine + " " + dataline
                    elif inLink:
                        currentLine = currentLine + dataline

                    # if in a commentedout block look for the ending
                    if inLink and re.match("\[\d+:", dataline):
                        inLink = False
                        currentLine = currentLine.replace('(/','(https://vimeo.com/')
                        links.append(currentLine)
                        currentLine = ""
            f.close()

    links.sort()
    return links

def translateFilesFromHtmlToMarkdown():
    path = "c:\\temp\\vimeolist"

    allFiles = os.listdir(path)
    for filename in allFiles:
        if filename.endswith(".txt"):
            with codecs.open(filename, "r",encoding='ascii', errors='ignore') as f:
                h = html2text.HTML2Text()
                data = f.read()
                body = h.handle(data)

                w = open(filename.replace('.txt','.new'),'w')
                w.write(body)
                w.close()
                f.close()


def main():
    translateFilesFromHtmlToMarkdown()
    links = processFilesIntoLinksList()
    readme = processReadMeIntoDictionary()

    for s in links:
        url = getUrlFromLine(s)
        if url not in readme:
            print('-',s)

if __name__ == "__main__":
    main()
