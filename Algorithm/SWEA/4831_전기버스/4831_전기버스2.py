

int N;
int m = 999999;
int Station[7] = { 0, 1,3,5,7,9, 10 };

void function1(int index , int count ) { # 충전기가 있는 곳들을 전부 다 탐색을 하는 재귀함수
    #예외케이스 집어넣기
    if(index ==6) {
         if ( m > count ) m = count;
        }

    
    for(int i=index + 1 ; i < 7; i++ ){
        station(i, count + 1) ;
        }
#버스가 뒤로 못가니까 백트래킹보다 완전탐색    
    }


main () { #완전탐색을 위한 메인
#    for(int i=0;i<6;i++ ) {
        function1(0,0);
#    } #예외가 필요하다. 처음에 도착하려고하는 충전기가 멀면 예외
    print m;
    }

#최소한, 최대한이 있을 때 완전 탐색
