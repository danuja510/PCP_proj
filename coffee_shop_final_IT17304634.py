product_list_arr = []
product_price_arr = []
extra_arr = []
multi_arr = []
product_tot_arr = []
counter = 0
power = 'n'
counter_2 = 0
counter_3 = 0
sub_tot = 0
while power == 'n':
        print('Welcome to Addis Coffee Shop')
        while counter < 14:
            print('1.Tea(milk) Rs.100')
            print('2.Coffee(Cream) Rs.200')
            print('3.Cappuccino(Cream) Rs.250')
            print('4.Latte(Cream) Rs.250')
            print('5.Hot Chocolate(Chocolate) Rs.250')
            print('6.Espresso(Cream) Rs.250')
            print('7.Chocolate chip cookie-2pc(Extra Cookie) Rs.150')
            print('Enter 8 To get the bill')
            print('If you want one item with extra and the same one without extra you have to enter them as two items')
            print('Maximum no. of items= 14(but you can get any no. of products)')
            print('tax = 4%')
            user_input = int(input('What would you like'))
            if user_input == 1:
                product_list_arr.append('Tea')
                product_price_arr.append(100)
                extra = int(input('Do you want milk? Enter 1 for Yes If No enter any other number'))
                multi = int(input('How many do you want'))
                multi_arr.append(multi)
                if extra == 1:
                    extra_arr.append('Extra Milk')
                    product_tot = (product_price_arr[counter] + 50) * multi
                else:
                    extra_arr.append('No Extra')
                    product_tot = product_price_arr[counter] * multi
                product_tot_arr.append(product_tot)
                temp1=counter
                counter = counter + 1
                user_input = 0
                extra = 0
                multi = 0
            else:
                if user_input == 2:
                    product_list_arr.append('Coffee')
                    product_price_arr.append(200)
                    extra = int(input('Do you want Cream? Enter 1 for Yes If No enter any other number'))
                    multi = int(input('How many do you want'))
                    multi_arr.append(multi)
                    if extra == 1:
                        extra_arr.append('Extra Cream')
                        product_tot = (product_price_arr[counter] + 50) * multi
                    else:
                        extra_arr.append('No Extra')
                        product_tot = product_price_arr[counter] * multi
                    product_tot_arr.append(product_tot)
                    temp1 = counter
                    counter = counter + 1
                    user_input = 0
                    extra = 0
                    multi = 0
                else:
                    if user_input == 3:
                        product_list_arr.append('Cappuccino')
                        product_price_arr.append(250)
                        extra = int(input('Do you want Cream? Enter 1 for Yes If No enter any other number'))
                        multi = int(input('How many do you want'))
                        multi_arr.append(multi)
                        if extra == 1:
                            extra_arr.append('Extra Cream')
                            product_tot = (product_price_arr[counter] + 50) * multi
                        else:
                            extra_arr.append('No Extra')
                            product_tot = product_price_arr[counter] * multi
                        product_tot_arr.append(product_tot)
                        temp1 = counter
                        counter = counter + 1
                        user_input = 0
                        extra = 0
                        multi = 0
                    else:
                        if user_input == 4:
                            product_list_arr.append('Latte')
                            product_price_arr.append(250)
                            extra = int(input('Do you want Cream? Enter 1 for Yes If No enter any other number'))
                            multi = int(input('How many do you want'))
                            multi_arr.append(multi)
                            if extra == 1:
                                extra_arr.append('Extra Cream')
                                product_tot = (product_price_arr[counter] + 50) * multi
                            else:
                                extra_arr.append('No Extra')
                                product_tot = product_price_arr[counter] * multi
                            product_tot_arr.append(product_tot)
                            temp1 = counter
                            counter = counter + 1
                            user_input = 0
                            extra = 0
                            multi = 0
                        else:
                            if user_input == 5:
                                product_list_arr.append('Hot Chocolate')
                                product_price_arr.append(250)
                                extra = int(input('Do you want a piece of Chocolate? Enter 1 for Yes If No enter any other number'))
                                multi = int(input('How many do you want'))
                                multi_arr.append(multi)
                                if extra == 1:
                                    extra_arr.append('Piece of Chocolate')
                                    product_tot = (product_price_arr[counter] + 50) * multi
                                else:
                                    extra_arr.append('No Extra')
                                    product_tot = product_price_arr[counter] * multi
                                product_tot_arr.append(product_tot)
                                temp1 = counter
                                counter = counter + 1
                                user_input = 0
                                extra = 0
                                multi = 0
                            else:
                                if user_input == 6:
                                    product_list_arr.append('Espresso')
                                    product_price_arr.append(250)
                                    extra = int(input('Do you want Cream? Enter 1 for Yes If No enter any other number'))
                                    multi = int(input('How many do you want'))
                                    multi_arr.append(multi)
                                    if extra == 1:
                                        extra_arr.append('Extra Cream')
                                        product_tot = (product_price_arr[counter] + 50) * multi
                                    else:
                                        extra_arr.append('No Extra')
                                        product_tot = product_price_arr[counter] * multi
                                    product_tot_arr.append(product_tot)
                                    temp1 = counter
                                    counter = counter + 1
                                    user_input = 0
                                    extra = 0
                                    multi = 0
                                else:
                                    if user_input == 7:
                                        product_list_arr.append('Chocolate Chip Cookie - 2pc')
                                        product_price_arr.append(150)
                                        extra = int(input('Do you want an extra Cookie? Enter 1 for Yes If No enter any other number'))
                                        multi = int(input('How many do you want'))
                                        multi_arr.append(multi)
                                        if extra == 1:
                                            extra_arr.append('Extra Cookie')
                                            product_tot = (product_price_arr[counter] + 50) * multi
                                        else:
                                            extra_arr.append('No Extra')
                                            product_tot = product_price_arr[counter] * multi
                                        product_tot_arr.append(product_tot)
                                        temp1 = counter
                                        counter = counter + 1
                                        user_input = 0
                                        extra = 0
                                        multi = 0
                                    else:
                                        if user_input == 8:
                                            temp1 = counter - 1
                                            temp2 = 14 - counter
                                            counter = counter + temp2
                                        else:
                                            print('Invalid Input')
        while counter_2 <= temp1:
            sub_tot = sub_tot + product_tot_arr[counter_2]
            counter_2 = counter_2 + 1
        tax = (4/100) * sub_tot
        tot = sub_tot + tax
        while counter_3 <= temp1:
            print(product_list_arr[counter_3],'  Rs.',product_price_arr[counter_3],'  +',extra_arr[counter_3], '  x',multi_arr[counter_3], '= Rs. ',product_tot_arr[counter_3])
            counter_3 = counter_3 + 1
        print('Sub Total - Rs.',sub_tot)
        print('tax - Rs.',tax)
        print('Your Total - Rs.',tot)
        print('Thanks For coming')
        counter = 0
        power = input('Enter n for a new bill or press any other button to close the program')





