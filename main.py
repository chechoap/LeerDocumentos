import PyPDF2
import docx

txt = 'prueba.txt'  # variable para guardar la ruta del archivo txt
pdf = 'while_loops.pdf'     #variable para guardar la ruta del archivo pdf
doc = 'ejemplo.docx'    #variable para guardar el archivo docx
cnt = 0     # cuenta cuantas veces se encuentra "busq" en cualquier archivo
busq = input("Texto a buscar: \n")      # la palabra o frase que el usuario va a buscar
total_times = 0     # contador del total de veces que aparece "busq" en cualquier archivo
pag_no = 0      # indica el numero de pagina (pdf) o el parágrafo (docx) en el que se encuentra actualmente buscando


def splitting_to_words(filepath, pag_no):
    with open(filepath, 'r') as txt:
        cnt = 0
        for line in txt:
            for word in line.split():
                if word == busq:
                    cnt += 1
    if cnt != 0:
        print("Se encontró(en la pag. no: "+str(pag_no)+"): "+str(cnt)+" veces.")
    return cnt


########## PDF ####################

def f_pdf(pdf, total_times, pag_no):
    print(" \n##### PDF #####")
    with open(pdf, 'rb') as pdf:
        pdf_read = PyPDF2.PdfFileReader(pdf)
        nopag = pdf_read.getNumPages()
        for i in range (nopag):
            page = pdf_read.getPage(i)
            content = page.extractText()
            with open('output.txt', 'w') as output:
                output.write(content)
                pag_no += 1
            total_times += splitting_to_words('output.txt', pag_no)
    return print("'"+busq+"' encontrado: "+str(total_times)+" veces en total en el archivo pdf.\n")


###################### DOCX ##############################

def f_docx(doc, total_times, pag_no):
    print("##### DOCX #####")
    document = docx.Document(doc)
    for paragraph in document.paragraphs:
        paragraph_text = paragraph.text
        with open('output.txt', 'w') as output:
            output.write(paragraph_text)
            pag_no += 1
        total_times += splitting_to_words('output.txt', pag_no)
    return print("'" + busq + "' encontrado: " + str(total_times) + " veces en total en el archivo dpcx")

##########################################################

f_pdf(pdf, total_times, pag_no)
f_docx(doc, total_times, pag_no)