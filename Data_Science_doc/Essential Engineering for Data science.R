iPreprocessing########################

######R as a Calculator######
2+2
2-3+1
2/3*2
2*3/2
2^3
2^3*2
2^(3*2)

###Mathematical functions in R
log(10);log(10,2) ##log(number,base)
sqrt(25)
sin(1)

# Some of the Built in constants

pi

LETTERS

letters

month.name

month.abb[12]

############################Data Types in R######################################
# a.  Numeric --real numbers 
# b.  Integer-- positive and negative whole  numbers including zero
# c.	logical-- True or False 
# d.	character-- alphabets/special characters
# e.	complex--  z<-1+2i;  Arg(0+1i); Mod(2-3i)

#Generating a sequence of numbers using scope operator and assigning to a variable
numbers<-10:15
numbers
#Generating a sequence of numbers using a "seq" function
numbers <- seq(1,10)
numbers
numbers<-seq(1,10,2) 
numbers

#Using  the "c" (concatenate) , we use this most of the time
numbers<-c(1,2,10)
numbers

#########################Variables in R########################################
# a.  Scalar -- a single number/character
x=5
x="a" 

#b.	Vector-- a sequence of elements
x<-c(1,2,3,4,5) 
x<-c("a","c")
y<-c("alpha",7)  
z <- c(T,F,TRUE,FALSE)


#To know the data type or class

class(z)


x <- c(1,3,5,7,9)

y <- c(2,4,6,8,10)

# Element wise addition

x+y

# Elementwise subtraction

x-y

# Elementwise multiplication

x * y 

# Elementwise division

x / y

########################################

x <- c(1,2,3,4,5,6)

y <- c(10,20) 

x + y # here vector y gets replicated so that vector addition be completed 


### Binding the vectors- Row binding and column binding

A <- rbind(x, y) 
A
B <- cbind(x, y)
B

# What if x<-c(1,2,3,4,5) and y<-c("a","b","c","d","e")

x <- c(1,2,3,4,5)

y <- c("a","b","c","d","e")

A <- rbind(x, y)  # observe the matrix data types

#c.  matrix--2d arrangement of elements (elements should be of same data type)

x <- matrix(c(1,2,3,4,5,6), nrow=3, ncol=2, byrow=T) #try with character data type
x

#Row sums and Column sums ,sum of diagonal elements, sum of all elements in Matrix

rowSums(x)

colSums(x)

sum(diag(x))

sum(x)

#d.  dataframe-- it is also a matrix representation but can have multiple data types in it.
##creating an empty data frame

data <-data.frame()

#Creating a data frame

data <- data.frame( Name=c("Alpha","Beta","Gamma"), 
                    Marks=c(29,NA,27)) 
data
#For both matrix and data frames: calling referring "elements" by position

x <- matrix(c(1,2,3,4), nrow=2, ncol=2, byrow=T)
x
x[1,1] # extracting element in first row and first column
x[1,]  #extracting all the elements from first row
x[,2]  #extracting all the elements from second column
x[2,1] #extracting  the element in second row and first column

#To get the dimensions of the matrix

dim(x)

#To name the rows or columns in the matrix
x
dimnames(x)<-list(c("One","Two"),c("Three","Four"))
x
data <- data.frame(Name=c("Alpha","Beta","Gamma"), Marks=c(29,30,27))

names(data)

names(data)<-c("Radiation", "Count")

data

#list-- a  "vector" containing other objects which could be a vector, a dataframe or a list.
#Creating a list

x <- c(1,2,3,4)

y <- c("a","b")

z <-  data.frame(name=c("Alpha","Beta","Gamma"), Marks=c(29,30,27))

A <- list(x,y,z)

#Try out the following and observe the output
A
A[1]
A[[1]]
A[1][1]
A[[1]][1]


#################Saving the work space as image, reading and loading data##################
# The workspace is your current R working environment and includes any user-defined
# objects (vectors, matrices, functions, data frames, and lists)
# The current working directory is the directory from which R will read files and to
# which it will save results by default. You can find out what the current working direc-
#   tory is by using the getwd() function. You can set the current working directory by
# using the setwd() function. If you need to input a file that isn't in the current working
# directory, use the full pathname in the call.

setwd("D:/Ravikanth/Academics/Batch25/20161211/ToShare/Data")

getwd()

#a.	Saving workspace

save.image() 

save.image("Save_20161211.RData")

# Loading saved workspace

load("Save_20161211.RData")

#b.	How do save only a few variables from environment

save(x, y, file="xy.RData")

#c.	Writing data to a file

write.csv(z,"./data.csv", row.names=F)  #for different delimited file ??

#d.	Reading the csv files and RData files into R environment

grade <- read.csv("./Grade.csv", header=T, sep = ",")

##Reading other formats we use read.table command  # comma as decimal & : as field sep ?

read <- read.table("./greek.txt",sep="\t",header=T)

# removing objects from the workspace

rm(x)

x  # Error: object 'x' not found

# remove all objects from the workspace

rm(list=ls(all=TRUE))

#########################################Subsetting###############################
##This might form an important aspect in Data analysis where we might want to work on a subset of data

##Subset on vectors
v<-c(1,2,3,4,5)
v[v>3]  #Output all elements greater than 3

attach(mtcars)
data<-mtcars

##Subset on matrices and data frames
#a. Calling by cell positions


data1<-data[,2:11]
data1<-data[1:10,2:11]

class(data1[,c(2,3)]) # explain this
data1[,1, drop=F] #droping str ?
#b. By using column names- two methods
data1<-data[,c("mpg","cyl")]

name<-c("mpg","cyl","disp","hp")
data1<-data[names(data) %in% name] ## %in% comes in handy for subsetting

#c. Using a subset function ##from help identify the argument to be given
data1<-subset(data,mpg>25,select=mpg:carb) #From data extracts all the records whose mpg>25 and all columns

#d. The same dataframe can be obtained in another way
data1<-data[mpg>25,]

##Multiple conditions can be given using "&" or "|"
data2<-data[mpg>25 & hp>75,]
data2<-subset(data,mpg>25 | gear==5,select=mpg:carb)

##Using which.max
data[which.max(mpg),]

##Using which.min
data[which.min(mpg),]

##Using which
data[which(data$mpg==max(data$mpg)),]
data[which(row.names(data) %in% c("Mazda RX4","Datsun 710")),]

detach(mtcars)

################################Data Exploration and Data Aggregation Methods#######################
##These form an important aspect especially for data exploration, data understanding and to processing
## the data for model building
##A data frame can have multiple datatypes in it like numeric, factor and logical.
library(plyr)
attach(baseball)
dfBB<-baseball
str(dfBB) ##outputs what to which type each variable belong to.
summary(dfBB) ## gives the overall summary of the data,we observe that the stats are given for numerical
## attributes, if characters then class and mode are mentioned.

##Conversion of variable types if necessary
##We can consider "teams" as a factor so that we can compare runs batted and home runs for teams
dfBB$team<-as.factor(dfBB$team)
str(dfBB$team)
##We do this appropriate conversions first

##Missing Values
##To count the number of missing values
sum(is.na(dfBB)) ##Gives the number of missing values in the data. What to do with the missing values ?

#option1. Omit all records with NA values
data1<-na.omit(dfBB)  ##it omits all the records which has atleast one NA value in it
data2<-dfBB[complete.cases(dfBB),]  ##another way

#Option2. If the missing values are few, then we can impute these missing values
library(DMwR)
data3<-centralImputation(dfBB) #Central Imputation
sum(is.na(data3))

data4<-knnImputation(dfBB[,-c(1,4,5)],scale=T,k=5) #KNN Imputation
sum(is.na(data4))

write.csv(data3, "data_imputed.csv", row.names=FALSE)

##several aggegation functions

##Using tapply, aggragate function and ddply
##tapply function is very flexible function for summerizing a vector x. 
tapply(dfBB$rbi,dfBB$team,FUN= sum,na.rm=T)

#aggregate(x,by,FUN,...)
aggregate(dfBB$rbi,by=list(dfBB$team),FUN=sum,na.rm=T)

##ddply
ddply(dfBB,.(team),summarize, runs=sum(rbi,na.rm=T))

##Please use R resources for exploring the above functions


##Randomly split  the data into two
rows<-seq(1,nrow(data),1)
set.seed(1234)
trainrows<-sample(rows,0.7*nrow(data))
Train<-data[trainrows,]
Test<-data[-trainrows,]




##############Working with the data ##########################
##There are several steps that we would follow for data preprocessing steps. These are not exhaustive 
##but according to the need we may use only some of these or sometimes we need to do a bit extra processing

##Understanding the data variables-- what are their types
##Data type conversions, if while loading the data the type taken is not appropriate
##Looking at the missing values  --either removing or imputing them
### Descriptive stats for distribution of data and for outlier detection
## Standardizing the data-- why scaling is important
#a. Using Standardization
#b. Using range
## Converting the variables 
#From Categorical to numeric  --Dummy
#From Numeric to categorical  -- Dicretizing (Equal Width, Equal Freq), Manual Coding

data <- read.csv(file="./dataMerged.csv",header=TRUE, sep=",")

#Undertanding data structure
str(data)
head(data)
tail(data)
edit(data)
names(data)
summary(data)

#Missing values handling

sum(is.na(data))#To check null values in data

#Dropping the recrods with missing values
data2<-na.omit(data)





#Standardizing the data
#Subsetting data
Data_NumAtr<-subset(data2,select=c(age,exp,inc,mortgage,ccAvg))
Data_CatAtr<-subset(data2,select=-c(age,exp,inc,mortgage,ccAvg))
library(vegan)
#Using range method
dataStd. <- decostand(Data_NumAtr,"range") 
summary(dataStd.)
#Using Z score method
dataStd. <- decostand(Data_NumAtr,"standardize")
summary(dataStd.)

#Discretizing the variable
summary(data2)
library(infotheo)
IncomeBin <- discretize(data2$inc, disc="equalfreq",nbins=4)
table(IncomeBin)
#tapply usage
tapply(data2$inc,IncomeBin,min)
tapply(data2$inc,IncomeBin,max)

IncomeBin <- discretize(data2$inc, disc="equalwidth",nbins=4)
table(IncomeBin)
#tapply usage
tapply(data2$inc,IncomeBin,min)
tapply(data2$inc,IncomeBin,max)



#Creating dummy variables and adding to original table
library(dummies)
EduDummyVars<-dummy(data2$edu)
head(EduDummyVars)
data2<-data.frame(data2,EduDummyVars)
head(data2)
