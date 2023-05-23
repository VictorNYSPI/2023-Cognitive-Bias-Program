You are likely to need to replace the path in setup.py to wherever this folder is located (by default it is set to your Documents folder)

If you wish to change the images used or in the folders, you will then need to run setup.py and:
* Run rate.html twice -- once for negative images, another time for positive
** rate.html will allow you to download a rating file each time it is run to completion, this should be moved to the Assets/Image Ratings folder (n.b. that both the positive and negative ratings should be done with the same user ID (or the file name itself can be changed))
* Run setup.py again
* Run abm.html or aat.html

Version Notes: 

amb works: 
240 presentations, 10 positive, 10 negative images, each picture appears 12 times, counterbalanced, cont/exp settings work 

aat works:
80 presentations, 10 positive, 10 negative images, each picture appears 4 times, 20 pos/push, 20 neg/push, 20 pos/pull, 20 neg/pull

Python scripts for R drive dir, tested 4.18.22


Notes: uses 10 pos/10 neg images, AAT and ABM work properly, tested last on 4.18.22