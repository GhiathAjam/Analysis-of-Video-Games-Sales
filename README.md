# Video Games Data Analysis 🕹️
Data science project to analyze and understand the global sales of video games across different genres and identify trends in consumer behavior. The goal of this analysis is to provide insights that can inform business decisions in the video game industry and help companies optimize their sales strategies.

# Project Pipeline ⚙️
  - Data Preprocessing
  - Data Exploration
  - Descriptive Analysis 
  - Exploratory Analysis
  - Predictive Analysis

# Data Preprocessing Approaches 🖥
  - Outliers Filteration
      * Drop All
      * Drop common outliers in all fields related to specific questions (useful as data contained too many outliers)
  - Nulls
      * Drop
      * Dope (mean, mode, ... )
  - Categoral features encoding

# Data Exploration 🔍

  - Discrete Features:
      
      <table>
      <tr>  <td>Name</td> <td>Developer</td> <td>Rating</td> <td>Publisher</td> <td>Genre</td>   </tr>       </table>
      - Rating: E (everyone), M(mature +17), T(teenagers) and E10+ (everyone +10)

  - Continous Features:
    * Sales in multiple regions
    * Global Sales (aggregate of previous)
    * Critic_Score: Aggregate score compiled by Metacritic staff.
    * Critic_Count: The number of critics used in coming up with the Critic_score.
    * User_Score: Score by Metacritic's subscribers
    * User_Count: Number of users who gave the user_score"""

  - Correlation between numerical features
    
![image](https://github.com/GhiathAjam/Analysis-of-Video-Games-Sales/assets/43111805/a0e9f511-ebea-445a-8ce8-655245d5be0d)


# Some analysis 📈

  - For games rated more than X, what is the most popular genre ?
    
  ![](https://github.com/GhiathAjam/Analysis-of-Video-Games-Sales/assets/43111805/65471cec-0a76-4998-b129-b674cc7579e8)

  - Do users or critics rate a specific platform or genre higher than others?

![image](https://github.com/GhiathAjam/Analysis-of-Video-Games-Sales/assets/43111805/eb09e27d-44f2-4ed2-8e95-d5d94fcdaa85)

  - For some specific game of multiple versions, Does rating get better or worse over time?
    
![](https://github.com/GhiathAjam/Analysis-of-Video-Games-Sales/assets/43111805/2082503f-d8cd-4c27-97ee-e01d76236076)

  - Compare platforms based on how long they stay competitive in the market.

  ![](https://github.com/GhiathAjam/Analysis-of-Video-Games-Sales/assets/43111805/64f2a198-d16c-4a51-8b37-92a1b0923a09)

  - Is there a certain publisher whose sales are most coming from a certain region?
    
![](https://github.com/GhiathAjam/Analysis-of-Video-Games-Sales/assets/43111805/ca660a88-2ee3-4ab8-91f6-937f1ebf740f)

  - For a specific genre, will its sales increase/decrease over the upcoming years?
    
 ![](https://github.com/GhiathAjam/Analysis-of-Video-Games-Sales/assets/43111805/359c508d-ca5f-4ed2-824f-a25154139532)

### Mechanistic
  -  How does the choice of platform affect sales for a specific genre?

![](https://github.com/GhiathAjam/Analysis-of-Video-Games-Sales/assets/43111805/03f579ff-1a4f-445a-92f6-23d916194d1e)

     1. PC & Strategy Games

    PC is a very very flexible platform and has a wide variety of setups, users basically create their dream platform using it.  
    Strategy games often involve a lot of observations and focus on signals and metrics with too much detail.  
    PC players can have a setup of more than one monitor for the details, observation, signals and metrics to watch out for.  
    PC players also have mouse, keyboard and even joystick to offer both precise and fast controls

    2. GBA & Platform

    GBA is a handheld console with D-pad and a very limited number of buttons, this makes it perfect for casual players who just want to plug-and-play with no hassle.  
    Platform games are usually played in short sessions, have basic movements and not very much is going on the screen.  
    Platform games could be fast-paced which requires fast controls.
    GBA also has a D-pad which is both fast to reach and precise to control.


### See the project document for all analysis details 📋

<!--
  - https://drive.google.com/drive/folders/1USOr-5aPy2-4Wn13b_IKpOFjs3goyDmx?usp=sharing
-->
  - [Report](./Deliverables/DS_Report18.pdf)
    
# Collaborators 👨🏻‍💻👩🏻‍💻

<table align="center">
<tr>
    <td align="center">
        <a href="https://github.com/GhiathAjam">
            <img src="https://avatars.githubusercontent.com/u/43111805?v=4" width="100;" alt="Gheiath"/>
            <br />
            <sub><b>Gheiath</b></sub>
        </a>
    </td>
   <td align="center">
        <a href="https://github.com/mohamed99akram">
            <img src="https://avatars.githubusercontent.com/u/69890013?v=4" width="100;" alt="mohamed99akram"/>
            <br />
            <sub><b>Mohamed Akram</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/mariemzayn18">
            <img src="https://avatars.githubusercontent.com/u/76264155?v=4" width="100;" alt="mariemzayn18"/>
            <br />
            <sub><b>Mariem Muhammed</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Marim1611">
            <img src="https://avatars.githubusercontent.com/u/76243256?v=4" width="100;" alt="Marim1611"/>
            <br />
            <sub><b>Marim Naser</b></sub>
        </a>
    </td>
   </tr>
</table>
