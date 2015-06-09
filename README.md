This is a changing Example Analysis for the FunTool. It may require some changes to work with the currently available versions. This will be updated when the FunTool hits version 1.0.

##How to download the FunTool!:

1.  Download python 3 from https://www.python.org/downloads/

2.  Open the terminal; run “pip3 install funtool” 

3.  Then run “pip3 install funtool_processes”

4.  Congratulations, you have just successfully downloaded the engine of the tool (funtool) and a collection of important and common functions to be used in an analysis (fun_tool processes). 

5. Now you need a way of telling the engine what to do and which functions to call in what order. To do so, you will need to download one more file, a template, or recipe list, written in simple markdown language (YAML)

6. Users of the FunTool! will change their templates often and so each template will be somewhat unique and likely changed often. Each user could rewrite their own template, but the developers of the FunTool! already provide an example analysis template that can be easily adjusted and repurposed.

7. There are several ways to download this example analysis template. 

  a.  If permitted by the developer of the FunTool!, you can navigate to the directory where you’d like to save the template (I recommend a FunTool! folder in your home directory) and enter “git clone git.all.usu:cyberlearning-funtool-analysis” 

  b.  An example of a FunTool! Analysis, which may be slightly outdated, is publicly available at https://github.com/pjanis/funtool-analysis

  c.  You can also receive the analysis template example personally from anyone who already has it. It does not need to be downloaded or installed.

##Theoretical Explanation of the FunTool!

The FunTool! takes data from a raw form then 1) adapts those data into a roughed form of data that can be used in the tool itself (this is equivalent to reading the data into memory) then 2) measures those data (using any number of pre-defined or custom measures) the 3) reports those data (usually in the form of a spreadsheet file such as tsv or csv files). See Figure 1 for a visual representation.
 
Figure 1. Visual representation of the FunTool!

Conceptually, the adaptor process and the reporting step are fairly simple, but the analysis stage can be quite complex. A very simple analysis consists of a datum being adapted, measured once, and then reported. For example, we could adapt a single JSON file from a Scratch save, then measure the number of sprites in that JSON file, then output a csv file showing that count.

Alternatively, and much more commonly, we would adapt a whole set of data including multiple Scratch users with multiple scratch projects over a series of time. Then, with this larger set of data, we could run a simple measure (like number of sprites) on the whole set of data then output a csv file showing the counts over time.

Let’s say we wanted to add a few more measures to our dataset. We could ask a variety of questions such as: 

1.  How many total blocks does each state have?
2.	What time was the project created?
3.	Is a certain block present?
4.	What is the ratio of one block to another?
5.	How often does a certain combination or sequence of blocks occur?

Furthermore, we don’t have to measure all of the states. If there was a certain group in which we were most interested (e.g. just a certain user, just a certain project or just certain sprites), we could select those groups then run measures on those groups. To illustrate, imagine I wanted to know the average number of “if/then” statements per sprite among a group of users with multiple projects. I would start by adapting all of the data, then measuring the if/then count for each state (using a state measure), then selecting only sprites (using a grouping selector), then measuring the average number of if/then statements for each sprite (using a group measure), then, finally, reporting the results. It can get a bit complicated, but remember, once you run the analysis correctly once, it can easily be repeated over and over with slightly different datasets. 


##How to use the FunTool!, Part 1: Geography of the FunTool!

For most practical purposes you do not need make any changes to the engine or the collection of processes (downloaded using the pip3 command earlier).  The analysis template, on the other hand, is where you will make most changes. Let’s take a look and explain what you will find in the example analysis directory:


1.	Analyses directory – This directory, one that we will alter frequently, contains a yaml file that contains the recipe list, or series of steps that will be called whenever the user runs their analysis. Typically, this yaml file calls for an adaptor to import data, a measure (or several measures) to analyze the data, a selector to grab certain groups of data, and a reporter to output the results in a useful format. More on that later.  

2.	Config directory – This directory, which contains several directories and yaml files (e.g. adaptors, analysis_selectors, group_measures, grouping_selectors, reporters, and state_measures), is where users can discover which processes are available to be called by their analysis yaml file (recipe list).

For example, in config>adaptors there is the folder_adaptor.yaml file which contains several types of adaptors (one to import a single directory of scratch json data from a particular location, one to import a directory with “project ID” sub-directories from a particular location, and one to import a directory with two sub-directories).

In config>state_measure there is the my_meaures.yaml file which contains an entire list of default state measure functions including measures to count different types of blocks, to calculate different ratios, to count scripts with certain features, and others.

In config>reporters there is the my_reporters.yaml file which contains a list of possible reporters such as state reporters and group reporters that produce tsv or csv files, reporters that report certain ratios, a reporter that produces plots, a reporter that randomly selects a certain state and shows the measurements so the user can manually check for tool errors, etc.

The config directory also includes analysis_selectors, grouping_selectors, and group_measures.
 
3.	Dashboard directory – This directory is still in development. It is meant to hold any code necessary to allow the FunTool! to reinterpret data output into dashboards. 

4.	Data directory – This directory is the default location for user data. Many adaptors point to this directory to find raw data.

5.	Logs directory – This directory contains detailed information about the history of the analysis process including time-stamped descriptions of functions called and versions used. Using information within this directory, researchers can retrace their steps and discover how their data analysis evolved overtime, an important step for reproduction and double-checking results.

6.	My_code directory – This directory is the default location for any user-created code (such as modifications or bug fixes) 

7.	Output directory – This directory contains the results from the reporters including a history of all outputs (commonly, these are spreadsheet files). 

8.	Readme.md file markdown file – Self-explanatory

9.	Run_analyses.py python file – Users will execute this python code to actually run the analysis once the analyses directory is properly modified and saved.

##How to use the FunTool!, Part 2: Importing Data

To import data, the user should place their raw data in the data directory, modify or write a new adaptor, then change the analyses template (or recipe list) to call the new or modified adaptor: The steps are listed below:

1.	Move data into the data directory within the example analysis (my example analysis is named funtool_analysis).

2.	Within the example analysis, open config>adaptors>folder_adaptor.yaml

3.	There are three types of adaptors (See Figure 4). One which imports a single directory (example_directory_adaptor), one which imports a directory which has project directories as sub-directories (example_projects_adaptor), and one that imports a directory that has user IDs as sub directories and project IDs as sub-sub-directories (example_users_adaptor).  
 
Figure 4. The three main adaptors for Scratch data.

4.	Copy the code for type of adaptor that matches your data (i.e. determine how many directories and sub-directories your raw data contains) and paste the copied code below the other adaptors. 

5.	Rename your new adaptor (e.g. delete “example_users_adaptor” and write “my_adaptor”), then adjust the data_location to account for the location of your raw data (data/<your data directory name here>).

6.	Save the yaml file.

7.	Navigate to my_analysis.yaml (your recipe list) within the analyses directory and replace the current adaptor with your new adaptor.

8.	Test your new adaptor by opening the terminal, navigating to the example analysis directory and running the python script run_analysis.py. This can be run using the terminal command “./run_analysis.py”.

9.	More complicated adaptors can be written to import any data  (besides Scratch data) as long as the data can be presented as a state. To do so, users can navigate to the appropriate code within funtool_processes (downloaded earlier using pip3) to see the underlying functions. Then, modeling those functions, users can add their own code to the my_code directory within the example analysis and call that code by changing the “adaptor_module” to point at the new code.
