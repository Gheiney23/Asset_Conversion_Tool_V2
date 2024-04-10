import pandas as pd
import PySimpleGUI as sg
from urllib.request import urlretrieve
import itertools as it

conv_df2 = {'Sku': [], 'Image_2_Name': [], 'Image_2_Failed': []}
conv_df3 = {'Sku': [], 'Image_3_Name': [], 'Image_3_Failed': []}
conv_df4 = {'Sku': [], 'Image_4_Name': [], 'Image_4_Failed': []}
conv_df5 = {'Sku': [], 'Image_5_Name': [], 'Image_5_Failed': []}
conv_df6 = {'Sku': [], 'Image_6_Name': [], 'Image_6_Failed': []}
specs_pdf_df = {'Sku': [], 'spec_File_name': [], 'Specs_Failed': []}
install_pdf_df = {'Sku': [], 'install_File_name': [], 'Install_Failed': []}
warranty_pdf_df = {'Sku': [], 'warranty_File_name': [], 'warranty_Failed': []}



def converter_tool(mfg_list_primary,
                   mfg_list_2,
                   mfg_list_3,
                   mfg_list_4,
                   mfg_list_5,
                   mfg_list_6,
                   Primary_url_list,
                   img_2_url_list,
                   img_3_url_list,
                   img_4_url_list,
                   img_5_url_list,
                   img_6_url_list,
                   folder_name):
    # Creating a folder variable for output
    output_directory = '{}'.format(folder_name)

    # Looping through the dictionary and creating jpgs from the urls and loading the file names into a list
    primary_df = {'Sku': [], 'Primary_File_name': [], 'Primary_Failed': []}

    for (mfg, url) in zip(mfg_list_primary, Primary_url_list):
        try:
            primary_file_name = mfg + '_Primary.jpg'
            urlretrieve(url, output_directory + f"\{primary_file_name}")
            primary_df['Primary_File_name'].append(primary_file_name)
            primary_df['Sku'].append(mfg)
            primary_df['Primary_Failed'].append('NULL')

        except:
            primary_df['Primary_Failed'].append(mfg)

    primary_df = pd.DataFrame.from_dict(primary_df).fillna('NULL')

    def dataframe2():
        global conv_df2

        for (mfg, url) in zip(mfg_list_2, img_2_url_list):
            try:
                file_name2 = mfg + '_img2.jpg'
                urlretrieve(url, output_directory + f"\{file_name2}")
                conv_df2['Image_2_Name'].append(file_name2)
                conv_df2['Sku'].append(mfg)
                conv_df2['Image_2_Failed'].append('NULL')

            except:
                conv_df2['Image_2_Failed'].append(mfg)

        conv_df2 = pd.DataFrame.from_dict(conv_df2).fillna('NULL')

    if any(mfg_list_2):
        dataframe2()
    else:
        global conv_df2
        conv_df2 = pd.DataFrame.from_dict(conv_df2).fillna('NULL')

    def dataframe3():
        global conv_df3

        for (mfg, url) in zip(mfg_list_3, img_3_url_list):
            try:
                file_name3 = mfg + '_img3.jpg'
                urlretrieve(url, output_directory + f"\{file_name3}")
                conv_df3['Image_3_Name'].append(file_name3)
                conv_df3['Sku'].append(mfg)
                conv_df3['Image_3_Failed'].append('NULL')

            except:
                conv_df3['Image_3_Failed'].append(mfg)

        conv_df3 = pd.DataFrame.from_dict(conv_df3).fillna('NULL')

    if any(mfg_list_3):
        dataframe3()
    else:
        global conv_df3
        conv_df3 = pd.DataFrame.from_dict(conv_df3).fillna('NULL')

    def dataframe4():
        global conv_df4

        for (mfg, url) in zip(mfg_list_4, img_4_url_list):
            try:
                file_name4 = mfg + '_img4.jpg'
                urlretrieve(url, output_directory + f"\{file_name4}")
                conv_df4['Image_4_Name'].append(file_name4)
                conv_df4['Sku'].append(mfg)
                conv_df4['Image_4_Failed'].append('NULL')

            except:
                conv_df4['Image_4_Failed'].append(mfg)

        conv_df4 = pd.DataFrame.from_dict(conv_df4).fillna('NULL')

    if any(mfg_list_4):
        dataframe4()
    else:
        global conv_df4
        conv_df4 = pd.DataFrame.from_dict(conv_df4).fillna('NULL')

    def dataframe5():
        global conv_df5

        for (mfg, url) in zip(mfg_list_5, img_5_url_list):
            try:
                file_name5 = mfg + '_img5.jpg'
                urlretrieve(url, output_directory + f"\{file_name5}")
                conv_df5['Image_5_Name'].append(file_name5)
                conv_df5['Sku'].append(mfg)
                conv_df5['Image_5_Failed'].append('NULL')

            except:
                conv_df5['Image_5_Failed'].append(mfg)

    if any(mfg_list_5):
        dataframe5()
    else:
        global conv_df5
        conv_df5 = pd.DataFrame.from_dict(conv_df5).fillna('NULL')

    conv_df5 = pd.DataFrame.from_dict(conv_df5).fillna('NULL')

    def dataframe6():
        global conv_df6

        for (mfg, url) in zip(mfg_list_6, img_6_url_list):
            try:
                file_name6 = mfg + '_img6.jpg'
                urlretrieve(url, output_directory + f"\{file_name6}")
                conv_df6['Image_6_Name'].append(file_name6)
                conv_df6['Sku'].append(mfg)
                conv_df6['Image_6_Failed'].append('NULL')

            except:
                conv_df6['Image_6_Failed'].append(mfg)

        conv_df6 = pd.DataFrame.from_dict(conv_df6).fillna('NULL')

    if any(mfg_list_6):
        dataframe6()
    else:
        global conv_df6
        conv_df6 = pd.DataFrame.from_dict(conv_df6).fillna('NULL')

    file_df = pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(primary_df, conv_df2,
                                                           how='left',
                                                           left_on='Sku',
                                                           right_on='Sku'),
                                                  conv_df3,
                                                  how='left',
                                                  left_on='Sku',
                                                  right_on='Sku'),
                                         conv_df4,
                                         how='left',
                                         left_on='Sku',
                                         right_on='Sku'),
                                conv_df5,
                                how='left',
                                left_on='Sku',
                                right_on='Sku'),
                       conv_df6,
                       how='left',
                       left_on='Sku',
                       right_on='Sku')

    Primary_Failed_col = file_df.pop('Primary_Failed')
    Image_2_Failed_col = file_df.pop('Image_2_Failed')
    Image_3_Failed_col = file_df.pop('Image_3_Failed')
    Image_4_Failed_col = file_df.pop('Image_4_Failed')
    Image_5_Failed_col = file_df.pop('Image_5_Failed')
    Image_6_Failed_col = file_df.pop('Image_6_Failed')

    file_df.insert(7, 'Primary_Failed', Primary_Failed_col)
    file_df.insert(8, 'Image_2_Failed', Image_2_Failed_col)
    file_df.insert(9, 'Image_3_Failed', Image_3_Failed_col)
    file_df.insert(10, 'Image_4_Failed', Image_4_Failed_col)
    file_df.insert(11, 'Image_5_Failed', Image_5_Failed_col)
    file_df.insert(12, 'Image_6_Failed', Image_6_Failed_col)

    file_df.fillna('NULL', inplace=True)

    #  Writing the dataframe to an excel worksheet
    file_df.to_excel('Image_Data.xlsx', sheet_name='File_Name_Data')

def pdf_tool(pdf_folder_name = [],
             spec_sku_list = [],
            install_sku_list = [],
            warranty_sku_list = [], 
            spec_url_list = [], 
            install_url_list = [], 
            warranty_url_list = []):

    df1 = {'Sku': [], 'Spec_File_name': [], 'Specs_Failed': []}
    df2 = {'Sku': [], 'Install_File_name': [], 'Install_Failed': []}
    df3 = {'Sku': [], 'warranty_File_name': [], 'warranty_Failed': []}

    output_directory = '{}'.format(pdf_folder_name)

    for (mfg, url) in zip(spec_sku_list, spec_url_list):
        try:
            specs_file_name = mfg + '_specification.pdf'
            urlretrieve(url, output_directory + f"\{specs_file_name}")
            df1['Sku'].append(mfg)
            df1['Spec_File_name'].append(specs_file_name)
            df1['Specs_Failed'].append('NULL')

        except:
            df1['Specs_Failed'].append(mfg)

    for mfg, url in it.zip_longest(install_sku_list, install_url_list, fillvalue='NULL'):
        try:
            install_file_name = mfg + '_installation.pdf'
            urlretrieve(url, output_directory + f"\{install_file_name}")
            df2['Sku'].append(mfg)
            df2['Install_File_name'].append(install_file_name)
            df2['Install_Failed'].append('NULL')

        except:
            df2['Install_Failed'].append(mfg)

    for (mfg, url) in zip(warranty_sku_list, warranty_url_list):
        try:
            warranty_file_name = mfg + '_warranty.pdf'
            urlretrieve(url, output_directory + f"\{warranty_file_name}")
            df3['Sku'].append(mfg)
            df3['warranty_File_name'].append(warranty_file_name)
            df3['warranty_Failed'].append('NULL')

        except:
            df3['warranty_Failed'].append(mfg)

    df1 = pd.DataFrame.from_dict(df1)
    df1 = df1.astype(str)
    
    df2 = pd.DataFrame.from_dict(df2)
    df2 = df2.astype(str)
    
    df3 = pd.DataFrame.from_dict(df3)
    df3 = df3.astype(str)
    
    file_df = pd.merge(pd.merge(df1, df2, how='left', left_on='Sku', right_on='Sku'), df3, how='left', left_on='Sku', right_on='Sku')

    specs_failed_col = file_df.pop('Specs_Failed')
    file_df.insert(3, 'Specs_Failed', specs_failed_col)
    file_df.fillna('NULL', inplace=True)

    # excel_wb = load_workbook(path)
    file_df.to_excel('PDF_Data.xlsx', sheet_name='PDF_File_Data')

    print('Run Complete!')



def make_main_window():
    # Theme of windows
    sg.theme('Dark Grey 13')

    # Creating window layouts
    main_layout = [[sg.Text("Team Product Tool")],
                   [sg.Text("Choose which tool you want.")],
                   [sg.Button("Image Converter Tool"), sg.Button("PDF Tool"),
                    sg.Button("Exit")]]

    return sg.Window('Main Window', main_layout)

def make_converter_window():
    # Theme of windows
    sg.theme('Dark Grey 13')
    # WORK HERE
    converter_layout = [[sg.Text("Image Converter Tool")],
                        # [sg.Text("Enter Skus and URLs for Primary images:")],
                        [sg.Text('Please enter Primary Sku(MFG Number) list.'), sg.InputText(key='-SKU-', pad=(0, 0))],
                        [sg.Text('Please enter Primary image URL list.'), sg.InputText(key='-URL-', pad=(0, 0))],
                        # [sg.Text("Enter Skus and URLs for 2nd image:")],
                        [sg.Text('Please enter Sku(MFG Number) list for 2nd image.'),
                         sg.InputText(key='-SKU2-', pad=(0, 0))],
                        [sg.Text('Please enter image URL list for 2nd image.'), sg.InputText(key='-URL2-', pad=(0, 0))],
                        # [sg.Text("Enter Skus and URLs for 3rd image:")],
                        [sg.Text('Please enter Sku(MFG Number) list for 3rd image.'),
                         sg.InputText(key='-SKU3-', pad=(0, 0))],
                        [sg.Text('Please enter image URL list for 3rd image.'), sg.InputText(key='-URL3-', pad=(0, 0))],
                        # [sg.Text("Enter Skus and URLs for 4th image:")],
                        [sg.Text('Please enter Sku(MFG Number) list for 4th image.'),
                         sg.InputText(key='-SKU4-', pad=(0, 0))],
                        [sg.Text('Please enter image URL list for 4th image.'), sg.InputText(key='-URL4-', pad=(0, 0))],
                        [sg.Text('Please enter Sku(MFG Number) list for 5th image.'),
                         sg.InputText(key='-SKU5-', pad=(0, 0))],
                        [sg.Text('Please enter image URL list for 5th image.'), sg.InputText(key='-URL5-', pad=(0, 0))],
                        [sg.Text('Please enter Sku(MFG Number) list for 6th image.'),
                         sg.InputText(key='-SKU6-', pad=(0, 0))],
                        [sg.Text('Please enter image URL list for 6th image.'), sg.InputText(key='-URL6-', pad=(0, 0))],
                        # [sg.Text('Please enter the absolute path of Excel file to use.'), sg.InputText(key='-E_NAME-')],
                        [sg.Text('Please enter the absolute path of folder to download images to.'),
                         sg.InputText(key='-F_NAME-')],
                        [sg.Button("Run"), sg.Button("Exit")]]

    convert_window = sg.Window('Image Converter Window', converter_layout, modal=True)

    while True:

        event, values = convert_window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break

        mfg_list_primary = values['-SKU-'].split('\n')
        mfg_list_2 = values['-SKU2-'].split('\n')
        mfg_list_3 = values['-SKU3-'].split('\n')
        mfg_list_4 = values['-SKU4-'].split('\n')
        mfg_list_5 = values['-SKU5-'].split('\n')
        mfg_list_6 = values['-SKU6-'].split('\n')
        Primary_list = values['-URL-'].split('\n')
        img_2_url_list = values['-URL2-'].split('\n')
        img_3_url_list = values['-URL3-'].split('\n')
        img_4_url_list = values['-URL4-'].split('\n')
        img_5_url_list = values['-URL5-'].split('\n')
        img_6_url_list = values['-URL6-'].split('\n')
        # excel_file_name = r'{}'.format(values['-E_NAME-'].rstrip())
        folder_name = r'{}'.format(values['-F_NAME-'].rstrip())

        if event == 'Run':

            try:
                # converter_tool(mfg_list_primary, mfg_list_2, mfg_list_3, mfg_list_4, Primary_list, img_2_list, img_3_list, img_4_list, folder_name)
                converter_tool(mfg_list_primary,
                               mfg_list_2,
                               mfg_list_3,
                               mfg_list_4,
                               mfg_list_5,
                               mfg_list_6,
                               Primary_list,
                               img_2_url_list,
                               img_3_url_list,
                               img_4_url_list,
                               img_5_url_list,
                               img_6_url_list,
                               folder_name)

                sg.popup("Run Complete!")
            except Exception as e:
                sg.popup("Something went wrong. Please make sure everything was entered correctly.", e)

    convert_window.close()

def make_pdf_window():
    # Theme of windows
    sg.theme('Dark Grey 13')

    img_layout = [[sg.Text("PDF Converter Tool")],
                  [sg.Text('Please enter spec sheet sku list.'), sg.InputText(key='-SPECSKU-', pad=(0, 0))],
                  [sg.Text('Please enter spec sheet URL list.'), sg.InputText(key='-SPECURL-', pad=(0, 0))],
                  [sg.Text('Please enter installation sheet sku list.'), sg.InputText(key='-INSTALLSKU-', pad=(0, 0))],
                  [sg.Text('Please enter installation sheet URL list.'), sg.InputText(key='-INSTALLURL-', pad=(0, 0))],
                  [sg.Text('Please enter warranty sheet sku list.'), sg.InputText(key='-WARSKU-', pad=(0, 0))],
                  [sg.Text('Please enter warranty sheet URL list.'), sg.InputText(key='-WARURL-', pad=(0, 0))],
                  [sg.Text('Please enter the absolute path of folder to download images to.'), sg.InputText(key='-F_NAME-')],
                  [sg.Button("Run"), sg.Button("Exit")]]

    image_window = sg.Window('PDF Converter Window', img_layout, modal=True)

    while True:

        event, values = image_window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break

        spec_url_list = values['-SPECURL-'].split('\n')
        install_url_list = values['-INSTALLURL-'].split('\n')
        warranty_url_list = values['-WARURL-'].split('\n')
        spec_sku_list = values['-SPECSKU-'].split('\n')
        install_sku_list = values['-INSTALLSKU-'].split('\n')
        warranty_sku_list = values['-WARSKU-'].split('\n')
        pdf_folder_name = r'{}'.format(values['-F_NAME-'].rstrip())

        if event == 'Run':

            try:
                pdf_tool(pdf_folder_name,
                        spec_sku_list, 
                        install_sku_list, 
                        warranty_sku_list, 
                        spec_url_list, 
                        install_url_list, 
                        warranty_url_list)
                
                sg.popup("Run Complete!")
            
            except Exception as e:
                sg.popup("Something went wrong. Please make sure everything was entered correctly.", e)

    image_window.close()


def main():
    # Theme of windows
    sg.theme('Dark Grey 13')

    # Creating window layouts
    main_layout = [[sg.Text("Team Product Tool")],
                   [sg.Text("Make sure you are on the VPN!", text_color='red', font=('Arial Bold', 10))],
                   [sg.Text("Choose which tool you want.")],
                   [sg.Button("Image Converter Tool"), sg.Button("PDF Converter Tool"),
                    sg.Button("Exit")]]

    main_window = sg.Window('Main Window', main_layout)

    # Event Loop
    while True:
        event, values = main_window.read()

        # End program if conditions met
        if event in (sg.WIN_CLOSED, "Exit"):
            break

        # Runs the Image URL Converter tool window and tool
        elif event == 'Image Converter Tool':
            make_converter_window()
        
        # Runs the PDF Converter tool window and tool
        elif event == 'PDF Converter Tool':
            make_pdf_window()

    main_window.close()


# Run the program
if __name__ == "__main__":
    main()