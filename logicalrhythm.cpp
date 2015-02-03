#include <stdio.h>
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

#define FOR(i,a,n) for(i=a;i<n;i++)
#define REP(i,n) for(i=0;i<n;i++)

ifstream train_orig_file("ocp_training.csv");
ofstream train_rem_comma("training.csv");
ifstream train_new_file("training.csv");
ifstream inp_orig_file("sampleinput.csv");
//ifstream inp_orig_file("ocp_testing.csv");
ofstream inp_rem_comma("in.csv");
ifstream inp_new_file("in.csv");
ifstream sample_output("sampleoutput.csv");
//ofstream sample_output("kaggleoutput.csv");

string s;

int freq[10][785][256], inp[785][256];  //freq[digit][pixel][grayscale]

int parse(int pos){
        
        int i=pos,num=0;
        while(i<s.size() && s[i]!=32){
                num = num*10 + s[i]-'0';
                i++;
        }
        return num;
}

int pos_of_next_space_plus_one(int pos){
        int i=pos;
        while(i<s.size() && s[i]!=32) i++;
        return ++i;
}

void rem_comma(ifstream &infile, ofstream &outfile){
        int i,j=0;
        while (getline(infile, s)){
                if(!j) {j++; continue;}
                for(i=0;i<s.size();i++){
                        if(s[i]==',') s[i] = 32;
                }
                outfile << s << endl;
        }       
}

void train_data(){
        
        int i,j,k=0,num;

        while (getline(train_new_file, s)){
                i=2;
                j = 1;
                while(i<s.size()){
                        freq[s[0]-'0'][j++][parse(i)]++;
                        i = pos_of_next_space_plus_one(i);
                }  
        }        
}

void solve(){
        //sample_output << "ImageId,Label" << endl;
        
        int i,j,k=10,gray,lo,hi,p,q,r=0,dig_at_pixel[785],ans,storeans[105],cnt_pixel_dig[10];
        long double score[10],temp,ma;
        
        int z = 0;
        
        while(getline(inp_new_file, s)){
                i = 2;
                j = 1;
                REP(p,10) score[p] = 0.0;
                while(i<s.size()){
                        gray = parse(i);
                        
                        p = 0;
                        while(gray-p && p<k) p++;
                        lo = gray - p;
                        p = 0;
                        while(gray+p<255 && p<k) p++;
                        hi = gray + p;
                        
                        REP(q,10){
                                FOR(p,lo,hi+1){
                                        score[q] += freq[q][j][p]*(p+1)*(p+1)/(abs(gray-p)+1);
                                }                
                        }
                        
                        j++;
                        i = pos_of_next_space_plus_one(i);
                }
                
                ma = -1.0;
                REP(p,10){
                        if(score[p]>=ma){
                                ma = score[p];
                                ans = p;
                        }
                }
                
                storeans[r++] = ans;
               
                //printf("%d\n",ans);
                //r++;
                //sample_output << r << "," << ans << endl; 
                
        }
        
        
        r=0;
        double total=0,correct=0;
        while(getline(sample_output,s)){
                total++;
                if(s[0]-'0'==storeans[r++]){
                        correct++;
                }
        }
        printf("Accuracy: %.2lf\n",(correct*100)/total);
 
}

int main(){
        
        int i,j;
        
        rem_comma(train_orig_file, train_rem_comma);
        rem_comma(inp_orig_file, inp_rem_comma);
        train_data();
        solve();
        
        /*       
        REP(i,10){
                REP(j,1){
                        cout << freq[i][2][j] << " ";
                }
                cout << endl;
        }*/

return 0;
}
