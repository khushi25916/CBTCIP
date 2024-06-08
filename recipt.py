from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


#data of transaction
data_name = [['product_name', 'product_quantity', 'price' , 'total_prize',], ["Product A", 2, 100,200],["Product B", 1, 150,150], ["Product C", 4, 100,400],["Product D", 1, 400,400],["Product E", 1, 500,500],["Product F", 3, 10,30],]

#generate pdf base 
pdf = SimpleDocTemplate("transaction_reciept.pdf",pagesize = A4)

#styling 
styles= getSampleStyleSheet()
custom_style = styles["Heading1"]
custom_style.alignment = 1
custom_style.textColor = colors.brown



# Create a paragraph with custom style
text = "TRANSACTION RECIEPT"
paragraph = Paragraph(text, custom_style)


#pattern of the table
style = TableStyle( 
    [ 
        (  "BOX" , ( 0, 0 ), ( -1, -1 ), 3 , colors.brown ), 
     #( "GRID" , ( 0, 0 ), ( 6, 6 ), 1 , colors.black ), 
     #( "BACKGROUND" , ( 0, 0 ), ( 5, 0 ), colors.blue), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.brown ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 0 ) , ( -1 , -1 ), colors.beige ), 
        ( "INNERGRID" , (0,0),(-1,-1),2,colors.brown)
    ] 
)  
table = Table(data_name,style=style)


#generate  pdf 
pdf.build([paragraph, table])

