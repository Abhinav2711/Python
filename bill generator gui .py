import os
import sys
import unittest

from reportlab.pdfgen import canvas

canvas = canvas.Canvas("form.pdf")
canvas.setLineWidth(.3)

def titleOfTicket():
    canvas.setFont('Helvetica', 12)
    canvas.drawString(30,750,'Bus Ticket')
    canvas.drawString(550,750,"Mr.X")

def header():
    canvas.line(30,740,580,740)
    canvas.drawString(30,723,"Bangalore to Chennai")
    canvas.drawString(250,723,"thu, 19 june 2017")
    canvas.drawString(450,723,"Trip ID 12345678901245")
    canvas.line(30,715,580,715)


titleOfTicket()
header()

canvas.save()
