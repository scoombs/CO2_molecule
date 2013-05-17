//program to stream coordinates file,calculate distance between atoms&plot
#include <fstream>
#include <cmath> 

using namespace std;
double x,y,z;
int i;
int  main()
{
     int num = 0; // num starts at 0,double floating pt prescion
     ifstream inputfile; //stream variable name is inputfile
     inputfile.open("coordinates"); //open file
     ofstream outfile; //stream variable name is outfile
     outfile.open("distances.txt");//open outfile

	while(!inputfile.eof()) //read numbers if not at the end of the inputfile
	{	
	inputfile >> x[num] >> y[num] >> z[num]; ++num;//this reads the 1st col number, the 2nd col number, etc, then goes to the next row	
	}

	o (i =0, i <= 199, i++)
	{
	array[i]; //defines array to store distances
	
	// Wish to find the bond lengths between C and each O, titled O1 and O2
	CO1_x[i] = x[3*i + 1] - x[3*i];
	CO2_x[i] = x[3*i + 2] - x[3*i];
	CO1_y[i] = y[3*i + 1] - y[3*i];
	CO2_y[i] = y[3*i + 2] - y[3*i];
	CO1_z[i] = z[3*i + 1] - z[3*i];
	CO2_z[i] = z[3*i + 2] - z[2*i];

	distanceO1 = sqrt(CO1_x[i]*CO1_x[i] + CO1_y[i]*CO1_y[i] + CO1_z[i]*CO1_z[i]); //distance between C and O1 
	distanceO2 =sqrt(CO2_x[i]*CO2_x[i] + CO2_y[i]*CO2_y[i]  + CO@_z[i]*CO2_z[i]); //distance between C and O2

        outfile << distance; //send distance data to outfile

	}

    outfile.close();
    inputfile.close();
    return 0;
}
