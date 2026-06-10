amount=int(input("Enter the amount:"))
gst=int(input("Enter the gst:"))
def mygst(amount,gst):
    cgst=(amount*gst)/100
    calc=amount+cgst
    return calc
ans=mygst(amount,gst)
print(ans)