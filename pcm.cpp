#include <iostream> 
#include <math.h> 

using namespace std;

class pcm{
    int amplitude, times;
    float freq;

public:

    pcm(){
        amplitude = 0;
        times =0;
        freq = 0;
    }

    void GetData(){
        cout<<"\nEnter 'amplitude': ";
        cin>>amplitude;
        cout<<"\nEnter 'frequency': ";
        cin>>freq;
        cout<<"\nEnter the no. of 'times' you want to run: ";
        cin>>times;
    }

    void Sampling(){
        for (int i = 0; i < times; ++i)
        {
            int rad;
            rad = ((2*3.14*freq*i)*(3.14))/180;
            cout<<"  "<<(amplitude*sin(rad));
            //cout<<amplitude<<endl<<freq<<endl<<times<<endl;
            //cout<<"  "<<(sin(2*3.14*freq*i));
            //cout<<"  "<<(amplitude*i);
        }
    }

};

int main(int argc, char *argv[])
{
    cout<<" -- Pulse Code Mod -- ";
    pcm sig;
    sig.GetData();
    sig.Sampling();
    return 0;
}
