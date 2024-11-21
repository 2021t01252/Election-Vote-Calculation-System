import mysql.connector
import matplotlib.pyplot as plt
class citizen:
    def __init__(self, nic, name, age, state):
        self.name = name
        self.nic = nic
        self.age = age
        self.state = state

    def register_citizen(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="",database="election")
            cursor = con.cursor()
            insert_citizen = "INSERT INTO citizen(nic, name, age, state) VALUES (%s,%s,%s,%s)"
            values=(self.nic,self.name,self.age,self.state)
            cursor.execute(insert_citizen,values)
            con.commit()
            print ("Register Successfull\n")
            menue()
        except:
            print("Database error\n")
            menue()



class candidate:

    def __init__(self,nic):
        self.nic=nic
        self.name=""
        self.age=""
        self.state=""
        self.education=""

    def load_data(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="election")
            cursor = con.cursor()
            get_candidateData = "SELECT * from citizen WHERE nic = " + self.nic + ""
            cursor.execute(get_candidateData)
            result = cursor.fetchall()
            if (result):
                for row in result:
                    self.name=row[1]
                    self.age=row[2]
                    self.state=row[3]
                    print(row)
            else:
                print("Invalid citizen\n")
                menue()
        except mysql.connector.Error as err:
            print("Database error",err,"\n")
            menue()



    def register(self,education,political_party_ID):
        self.education=education
        self.political_party_ID=political_party_ID
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="",database="election")
            cursor = con.cursor()
            insert_candy = "INSERT INTO candidate(nic, name, age, education,state,poli_id) VALUES (%s,%s,%s,%s,%s,%s)"
            values=(self.nic,self.name,self.age,self.education,self.state,self.political_party_ID)
            cursor.execute(insert_candy,values)
            con.commit()
            print ("Register Successfull\n")
            menue()
        except:
            print("Database error\n")
            menue()

    def showParty(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="election")
            cursor = con.cursor()
            get_poliData = "SELECT * from poli_party"
            cursor.execute(get_poliData)
            result = cursor.fetchall()
            if (result):
                for row in result:
                    print(row)
            else:
                print("There are no any party registered\n")
                menue()
        except:
            print("Database error\n")
            menue()

class poliparty:
    def __init__(self,poli_name):
        self.poli_name=poli_name

    def register_party(self):
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="election")
            cursor = con.cursor()
            insert_pol = "INSERT INTO poli_party(poli_id,poli_name) VALUES (%s,%s)"
            values = ("",self.poli_name)
            cursor.execute(insert_pol,values)
            con.commit()
            print("Register Successfull\n")
            menue()
        except:
            print("Database error\n")
            menue()



def menue():
    print("-----------Welcome to election voting system-----------\n")
    print("1.Register a citizen")
    print("2.Register a candidate")
    print("3.Register a political party")
    print("4.Voting")
    print("5.count")

    selector=int(input("Enter your selection: "))
    print("\n")

    if(selector==1):
        nic=str(input("Enter your nic number: "))
        name=str(input("Enter your name: "))
        age=int(input("Enter your age: "))
        state=str(input("Enter your state: "))
        if(age>18 and nic!="" and name!="" and state!=""):
            newcitizen = citizen(nic, name, age, state)
            newcitizen.register_citizen()
        else:
            print("You are not eligible for the registration\n")
            menue()

    elif(selector==2):
        nic=str(input("Enter Candidate nic: "))
        newcandidate=candidate(nic)
        newcandidate.load_data()
        selector = int(input("\nDo you want to registor this candidate yes=1 No=2 : "))
        if(selector==1):
            newcandidate.showParty()
            education=str(input("Enter educational qualifications : "))
            political_party_id = int(input("Select above political party number : "))
            newcandidate.register(education,political_party_id)

        else:
            menue()

    elif (selector == 3):
        party=str(input("Enter the political party name : "))
        newpoli_party=poliparty(party)
        newpoli_party.register_party()

    elif (selector==4):
        nic=str(input("Enter your nic no : "))
        voting(nic)

    elif (selector==5):
        count_votes()


def voting(nic):
        voteNo = []
        global state
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="election")
            cursor = con.cursor()
            get_citizenData = "SELECT * from citizen WHERE nic = " + nic + ""
            cursor.execute(get_citizenData)
            result = cursor.fetchall()
            if (result):
                for row in result:
                    state=row[3]
                    print("Citizen details:-",row,"\n\n")
                get_candidateData = "SELECT *,poli_name from candidate,poli_party where candidate.poli_id=poli_party.poli_id"
                cursor.execute(get_candidateData)
                result1 = cursor.fetchall()
                for row1 in result1:
                    print("Candidate Id:-",row1[0])
                    print("Candidate state:-",row1[5],"\nCandidate political party:-",row1[8],"\n")
                for x in range(3):
                    vote = int(input("Enter the candidate ID that you want to vote: "))
                    voteNo.append(vote)
                setVote(voteNo,nic)
            else:
                print("Invalid citizen\n")
                menue()
        except:
            print("Database error\n")
            menue()

def setVote(voteNo,nic):
    con = mysql.connector.connect(host="localhost", user="root", password="", database="election")
    cursor = con.cursor()
    insert_vote = "INSERT INTO voting(nic,vote1,vote2,vote3) VALUES (%s,%s,%s,%s)"
    values = (nic,voteNo[0],voteNo[1],voteNo[2])
    cursor.execute(insert_vote, values)
    con.commit()
    print("voting Successfull\n")
    menue()

def count_votes():
        try:
            con = mysql.connector.connect(host="localhost", user="root", password="", database="election")
            cursor = con.cursor()
            get_votes = "SELECT vote1, vote2, vote3 FROM voting"
            cursor.execute(get_votes)
            result = cursor.fetchall()
            vote_counts = {}
            for row in result:
                for candidate_id in row:
                    if candidate_id in vote_counts:
                        vote_counts[candidate_id] += 1
                    else:
                        vote_counts[candidate_id] = 1

            sorted_vote_counts = sorted(vote_counts.items(), key=lambda x: x[1], reverse=True)

            candidate_names = []
            votes = []
            for candidate_id, count in sorted_vote_counts:
                get_candidate_name = f"SELECT name FROM candidate WHERE can_id = {candidate_id}"
                cursor.execute(get_candidate_name)
                candidate_name = cursor.fetchone()[0]
                candidate_names.append(candidate_name)
                votes.append(count)

            plt.bar(candidate_names, votes)
            plt.xlabel('Candidates')
            plt.ylabel('Votes')
            plt.title('Election Results')
            plt.show()
            menue()

        except mysql.connector.Error as err:
            print("Database error\n")
            menue()

menue()