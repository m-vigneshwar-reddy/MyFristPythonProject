'''
this program is the part of my csp project where I made the mini-project that can help the formers on desiding on which
crop ,they can grow based on what type of crop they choice and the fertilzer and how much time they have to grow the
crop
        Based on what they select  and the data on the crops I have on the excel sheets the program will show
some of the crops that may meat the user requirments

        here the user can select one of the three classification option
        (
        1. TYPE OF THE CROP
        2. FERTILIZER THE USER CAN USE
        3. THE TIME DURATION THAT THE USER CAN GROW THE CROP FOR
        )
1. on the base of my knowledge I classified the types of crops in to 6 types
   1. Food CROPS
   2. Feed CROPS
   3. Fiber CROPS
   4. Oil CROPS
   5. Ornamental CROPS
   6. Industrial CROPS

And 2 . is based on the fertilizers that the former may have with in his hands
  and most of the fertilizers that can be used on crops are
        1.Nitrogen-based fertilizers
        2.Phosphorus-based fertilizers
        3.Potassium-based fertilizers

        At lost 3 option the time duration that the former has to grow the cropthe reason that I added this option is
becouse the time and sessions play an important role on crop growth  and not to know when to harvest  is  important .
if the user take more or less time than they should it may effcat some problems on the harvest so knowing the duration
of the crop is also important

        hence thay  are the 3 options for the user to select in this program  and based on what the former select the
crops will be selected
'''
import pandas as pd
data = pd.read_csv("../../vig/cp/crop_information_with_season_soil.csv")
pd.set_option('display.max_columns',10)
#-----------------
# lets know on what based on what do the user wants to know the crops
# Note : at the end of the program we will at the user know all the facters of the crop
#-----------------
ch = int(input("  do you want to know the crop on based on \n 1. type of the crop\n 2.the fertilzer you have"
               "\n 3. time the crop you have to grow and hervest "
               "\n Note:we will give you all the about data on the crops after the selection"
               "\n Enter your choice(1 or 2 or 3): "))
if ch == 1:
    #-------
    #lets know which type of crop do the user want to know about?:
    #-------------------
    i_crop=int(input("select the type of the crop:\n1.Cash CROP \n2.Cereal CROP\n3.Fiber CROP\n4.Fruit CROP\n5.Legume CROP"
                     "\n6.Vegetable CROP\n\n\n enter your choice:  "))
    crops=['Cash','Cereal','Fiber','Fruit' ,'Legume' ,'Vegetable']
    print(data[['Crop Name','type','Type of Fertilizer','Time Duration' ]][data["type"]== crops[i_crop-1]])
elif ch == 2:
    #----------------
    #lets know which fertilizer done the user has with him
    #---------------
    i_fert= int(input("select the  frertilizer you have:\n1.Nitrogen-based fertilizers\n2.Phosphorus-based fertilizers"
                  "\n3.Potassium-based fertilizers\n Ehter your choice: "))
    fert=('Nitrogen-based fertilizer','Phosphorus-based fertilizer','Potassium-based fertilizer')
    print(data[['Crop Name','type','Type of Fertilizer','Time Duration' ]][data["Type of Fertilizer"] == fert[i_fert - 1]])
elif ch == 3:
    #---------------
    # let know the time user have to grow the crop
    #-----------------
    i_time = float(input("\n\ncan I know the time you have to grow the crop:  "))
    print(data[['Crop Name','type','Type of Fertilizer','Time Duration' ]][data['Time Duration for Harvest']<=i_time]
          .sort_values('Time Duration for Harvest'))
else:
    print("noties: sorry,you have entered the wrong option!!")