def currency_converter():
    while True:
        try:
            in_dollar=int(input("enter your currency in dollar:"))
            break
        except:
            print("Please try again :")
    print("Select the currency form to which you want your dollar to be converted:\n" \
          "1 for European Euro(Eur)\n" \
          "2 for Japanese Yen(JPY)\n" \
          "3 for British Pound(GBP)\n" \
          "4 FOR Saudi reyal(SAR)\n" \
          "5 for Vietnamese Dong(VND)\n" \
          "6 for Yemini Riyal(rial)"
          "7 for Indian Rupee(INR)\n" \
          "8 for Pakisthani Rupee(PKR)\n" \
          "9 for UAE Dirham(AED)\n"
          )
    conversion_to=int(input("select from the above listed values:"))
    if(conversion_to==1):
        print(in_dollar," $ in euro:",in_dollar*0.88)
    elif(conversion_to==2):
        print(in_dollar,"$ in JPY",in_dollar*107.24)
    elif (conversion_to == 3):
        print(in_dollar, "$ in GBP",in_dollar*0.80)
    elif (conversion_to == 4):
        print(in_dollar, "$ in SAR",  in_dollar*3.75)
    elif (conversion_to == 5):
        print(in_dollar, "$ in VND",  in_dollar*3.75)
    elif (conversion_to == 6):
        print(in_dollar, "$ in RIAL",  in_dollar*250.40)
    elif (conversion_to == 7):
        print(in_dollar, "$ in INR",  in_dollar*74.97)
    elif (conversion_to == 8):
        print(in_dollar, "$ in PKR",  in_dollar*167.52)
    elif (conversion_to == 9):
        print(in_dollar, "$ in AED", in_dollar*3.67)
    else:
        ('Kindly select the value within the given options.')

while True:
    currency_converter()
    rerun_or_not = input("Do you want to use converter again? yes/no")
    if rerun_or_not=='yes' or rerun_or_not=='YES' or rerun_or_not=="y" or rerun_or_not=="Y"or rerun_or_not=="Yes":
        continue
    else:
        print("Thanku for using our converter.Have a nice day")
        break
