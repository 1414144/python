from tkinter import *

windows=Tk()
windows.title("Identificacion de estudiantes")
windows.geometry("900x600")
windows.configure(bg="cyan")
titulo=Label(windows,text="indentificación de estudiantes",font=("cooper blak",16,"bold"),bg="cyan")
titulo.place(x=10,y=20)
titulo=Label(windows,text="Identificación:",bg="cyan")
titulo.place(x=10,y=60)
txt_Identificación=Entry(windows,width=20)
txt_Identificación.place(x=100,y=60)
titulo=Label(windows,text="Nombre completo:",bg="cyan")
titulo.place(x=8,y=90)
txt_nome=Entry(windows,width=20)
txt_nome.place(x=120,y=90)
titulo=Label(windows,text="Sección:",bg="cyan")
titulo.place(x=270,y=90)
txt_sec=Entry(windows,width=10)
txt_sec.place(x=320,y=90)
#########################################################################################################################################
bd_datos={"123":"keneth duarte","456":"juan manuel"}
bd_sec={"123":"10-1","456":"10-2"}
bd_espa_tc={"123":"25","456":"30"}
bd_espa_ta={}
#########################################################################################################################################
def consultar_datos():
    txt_nome.insert(0,bd_datos[txt_Identificación.get()])
    txt_sec.insert(0,bd_sec[txt_Identificación.get()])
    txt_ESPA_tc.insert(0,bd_espa_tc[txt_Identificación.get()])
boton_Bus=Button(windows,text="Consultar", command=consultar_datos)
boton_Bus.place(x=320,y=50)
titulo=Label(windows,text="Desglose de Nota por Materia",font=("cooper blak",16,"bold"),bg="cyan")
titulo.place(x=8,y=130)
titulo=Label(windows,text="Materia",bg="cyan")
titulo.place(x=8,y=180)
titulo=Label(windows,text="TC",bg="cyan")
titulo.place(x=100,y=180)
titulo=Label(windows,text="Tarea",bg="cyan")
titulo.place(x=160,y=180)
titulo=Label(windows,text="Proyecto",bg="cyan")
titulo.place(x=230,y=180)
titulo=Label(windows,text="Prueba 1",bg="cyan")
titulo.place(x=310,y=180)
titulo=Label(windows,text="prueba 2",bg="cyan")
titulo.place(x=380,y=180)
titulo=Label(windows,text="Asistencia",bg="cyan")
titulo.place(x=450,y=180)
titulo=Label(windows,text="Promedio",bg="cyan")
titulo.place(x=530,y=180)
#########################################################################################################################################
titulo=Label(windows,text="Español",bg="cyan")
titulo.place(x=8,y=210)
titulo=Label(windows,text="Fisica Mate",bg="cyan")
titulo.place(x=8,y=250)
titulo=Label(windows,text="Matematicas",bg="cyan")
titulo.place(x=8,y=290)
titulo=Label(windows,text="Estudios Sociales",bg="cyan")
titulo.place(x=4,y=330)
#########################################################################################################################################
txt_ESPA_tc=Entry(windows,width=5)
txt_ESPA_tc.place(x=100,y=210)
txt_ESPA_ta=Entry(windows,width=5)
txt_ESPA_ta.place(x=160,y=210)
txt_ESPA_proy=Entry(windows,width=5)
txt_ESPA_proy.place(x=230,y=210)
txt_ESPA_exa1=Entry(windows,width=5)
txt_ESPA_exa1.place(x=310,y=210)
txt_ESPA_exa2=Entry(windows,width=5)
txt_ESPA_exa2.place(x=380,y=210)
txt_ESPA_asis=Entry(windows,width=5)
txt_ESPA_asis.place(x=450,y=210)
txt_ESPA_prom=Entry(windows,width=5)
txt_ESPA_prom.place(x=530,y=210)

txt_FISICA_tc=Entry(windows,width=5)
txt_FISICA_tc.place(x=100,y=250)
txt_FISICA_ta=Entry(windows,width=5)
txt_FISICA_ta.place(x=160,y=250)
txt_FISICA_proy=Entry(windows,width=5)
txt_FISICA_proy.place(x=230,y=250)
txt_FISICA_exa1=Entry(windows,width=5)
txt_FISICA_exa1.place(x=310,y=250)
txt_FISICA_exa2=Entry(windows,width=5)
txt_FISICA_exa2.place(x=380,y=250)
txt_FISICA_asis=Entry(windows,width=5)
txt_FISICA_asis.place(x=450,y=250)
txt_FISICA_prom=Entry(windows,width=5)
txt_FISICA_prom.place(x=530,y=250)

txt_MATE_tc=Entry(windows,width=5)
txt_MATE_tc.place(x=100,y=290)
txt_MATE_ta=Entry(windows,width=5)
txt_MATE_ta.place(x=160,y=290)
txt_MATE_proy=Entry(windows,width=5)
txt_MATE_proy.place(x=230,y=290)
txt_MATE_exa1=Entry(windows,width=5)
txt_MATE_exa1.place(x=310,y=290)
txt_MATE_exa2=Entry(windows,width=5)
txt_MATE_exa2.place(x=380,y=290)
txt_MATE_asis=Entry(windows,width=5)
txt_MATE_asis.place(x=450,y=290)
txt_MATE_prom=Entry(windows,width=5)
txt_MATE_prom.place(x=530,y=290)

txt_ESTU_tc=Entry(windows,width=5)
txt_ESTU_tc.place(x=100,y=330)
txt_ESTU_ta=Entry(windows,width=5)
txt_ESTU_ta.place(x=160,y=330)
txt_ESTU_proy=Entry(windows,width=5)
txt_ESTU_proy.place(x=230,y=330)
txt_ESTU_exa1=Entry(windows,width=5)
txt_ESTU_exa1.place(x=310,y=330)
txt_ESTU_exa2=Entry(windows,width=5)
txt_ESTU_exa2.place(x=380,y=330)
txt_ESTU_asis=Entry(windows,width=5)
txt_ESTU_asis.place(x=450,y=330)
txt_ESTU_prom=Entry(windows,width=5)
txt_ESTU_prom.place(x=530,y=330)

#########################################################################################################################################

##############################################################################################################################################################

















