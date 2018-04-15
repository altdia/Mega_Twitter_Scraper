TRACK_TERMS = ["#GodBless", "#CrisisActor", "#CrisisActors", "#ForGodAndCountry", "#AmericanHeroes", "#ReleaseTheCures", "#MAGA", "#GreatAwakening", "#WeThePeople", "#FakeNews", "#Treason", "#ReleaseEverything", "#QAnon", "#AmericaFirst", "#ObamaGate","#ReleaseTheFootage", "#Qanon8chan", "#tillerson","Trump", "Tillerson", "North Korea", "Russia", "Clinton", "Illegal Immigrants", "#Q", "election"]
CONNECTION_STRING = "postgresql://username:password@host:port/database"
CSV_NAME = "bots.csv"
TABLE_NAME = "botpull"

try:
    from private import *
except Exception:
    pass
