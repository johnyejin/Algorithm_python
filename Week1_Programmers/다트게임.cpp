#include <string>
#include <cmath>
using namespace std;

int solution(string dartResult) {
    int answer = 0;
    int temp[3] = {0,};
    int cnt = 0;
    
    for(int i=0; i<dartResult.size();) {
        
        if(dartResult[i] >= 48 && dartResult[i] <= 57) {
            // 숫자가 10인 경우 예외처리
            if(dartResult[i+1] == '0') {
                temp[cnt] = 10;
                i += 2;
                cnt++;
                continue;
            }
            temp[cnt] = dartResult[i] - '0';
            cnt++;
        } 
        else if (dartResult[i] == 'S') {
            temp[cnt-1] = pow(temp[cnt-1], 1);
        } else if (dartResult[i] == 'D') {
            temp[cnt-1] = pow(temp[cnt-1], 2);
        } else if (dartResult[i] == 'T') {
            temp[cnt-1] = pow(temp[cnt-1], 3);
        } 
        else if (dartResult[i] == '*') {
            temp[cnt-1] *= 2;
            temp[cnt-2] *= 2;
        } 
        else if (dartResult[i] == '#') {
            temp[cnt-1] = temp[cnt-1] * (-1);
        }
        i++;
    }
    
    for(int i=0; i<3; i++) {
        answer += temp[i];
    }
    
    return answer;
}
