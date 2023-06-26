# Insights of Best CS Scientists Worldwide

In this project, I gather information from [this site](https://research.com/scientists-rankings/computer-science). After fetching data, I show the below insights in Tableau.

1. Max Citations Per Country.
2. Comparison among Citations, No of Publications and H-index.
3. Max Publications Per University in Asia.
4. No of Scientists in Asia and Middle East Countries.

You can see the findings from [here](https://public.tableau.com/app/profile/md.tanvir.hossain/viz/Demoprojectofbestcsscientistsdatasetmine/Dashboard1).

## Findings

1. Mostly European country gets the highest citations. Canada is top of them.
2. In most of the case, if citations is high, H-index is also high of those university and vice-versa. Those university are in the top who has high H-index and citations.
3. Chineses university has the top publications in Asia. Some university from Hong-kong, Japan, India are Taiwan are also take a place in the list.
4. Here also China has the most CS scientists among Asia & Middle Eastern countries. 


## Build and Run the Code

1. Clone the repository
   `git clone https://github.com/MdTanvirHossainTusher/Tableau-project.git`

2. Create a virtual environment with these commands in windows-
   `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
   `.\venv\Scripts\activate`

3. Install selenium and pandas into the virtual environment by the below commands-
   `pip install selenium`
   `pip install pandas`

4. Run `main.py` with this command-
   `python scraper(cs scientists details).py`

5. To deactivate the virtual environment type this command-
   `deactivate`

6. Import `best_cs_scientists_details.csv` file in the Tableau and make changes according to [this](https://public.tableau.com/app/profile/md.tanvir.hossain/viz/Demoprojectofbestcsscientistsdatasetmine/Dashboard1) to get the findings.

N.B: This project is slightly different from [this project](https://github.com/msi1427/Demographics-of-Best-CS-Scientists-Worldwide). Main idea is taken form that project.
