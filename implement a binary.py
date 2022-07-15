def dec(num):
    if num >=1:
        dec(num //2)
    print(num % 2, end ='')
if __name__ =="__main__":
    dec_val = 24
    dec(dec_val)
    





