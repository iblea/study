#include <gtest/gtest.h>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

/*
문제 설명
고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.

고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

제한사항

차량의 대수는 1대 이상 10,000대 이하입니다.
routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.
 */

int solution(vector<vector<int>> routes) {
    int answer = 1;

    // 첫 번째 인덱스를 기준으로 오름차순 정렬
    sort(routes.begin(), routes.end());

    // 카메라 위치를 찍을 수 있는 위치를 찾는다.
    int camera = routes[0][1];

    for (int i = 1; i < routes.size(); i++) {
        // 카메라 위치보다 다음 차량의 시작 위치가 더 크다면 카메라 위치를 변경한다.
        if (camera < routes[i][0]) {
            camera = routes[i][1];
            answer++;
        }
        // 카메라 위치보다 다음 차량의 시작 위치가 작다면 카메라 위치를 변경하지 않는다.
        // 반례 케이스 대처: [[15,20], [16,17]]
        else {
            camera = min(camera, routes[i][1]);
        }
    }
    return answer;
}

#define CLASS_NAME gtest_template

class CLASS_NAME: public ::testing::Test {
private:
	clock_t t0;
	clock_t t1;
protected:
	CLASS_NAME() { }
	~CLASS_NAME() override { }

	void SetUp() override { set_start_time(); }
	void TearDown() override { set_end_time(); get_duration_time(); }

	void set_start_time() {
		this->t0 = clock(); // or gettimeofday or whatever
	}
	void set_end_time() {
		this->t1 = clock(); // or gettimeofday or whatever
	}

	// 시간 관련 체크
	void get_duration_time() {
		double elapsedSec = (double)(this->t1 - this->t0) / (double)1000000;
		double elapsedMS = (double)(this->t1 - this->t0) / (double)1000;

		cout << setprecision(3) << fixed << endl << "Duration of Times : ";
		cout << elapsedMS << "ms, " << elapsedSec << "sec" << endl << endl;
	}

};

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution({ { -20,-15 }, { -14,-5 }, { -18,-13 }, { -5,-3 } } ), 2);
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
