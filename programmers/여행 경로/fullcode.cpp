#include <gtest/gtest.h>
#include <iostream>

#include <string>
#include <vector>
using namespace std;

/*
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
*/
#include <iomanip>
#include <algorithm>
#include <map>
vector<string> solution(vector<vector<string>> tickets) {

    map<string, vector<string>> m = map<string, vector<string>>();

    for (vector<string> ticket : tickets) {
        if (m.find(ticket[0]) == m.end()) {
            m[ticket[0]] = vector<string>();
        }
        m[ticket[0]].push_back(ticket[1]);
    }

    // m을 순회하며 알파벳 순으로 정렬
    for (auto &it : m) {
        sort(it.second.begin(), it.second.end(), greater<string>());
    }

    vector<string> path = { "ICN" };
    vector<string> answer;

    while (! path.empty()) {
        string last = path.back();
        if (m.find(last) == m.end() || m[last].empty()) {
            path.pop_back();
            answer.insert(answer.begin(), last);
        } else {
            path.push_back(m[last].back());
            m[last].pop_back();
        }
    }
    return answer;
}
/*
M
ICN = [SFO, ATL]
ATL = [SFO, ICN]
SFO = [ATL]
path=[ "ICN" ]

ICN = [SFO]
ATL = [SFO, ICN]
SFO = [ATL]
path=[ "ICN", "ATL" ]

ICN = [SFO]
ATL = [SFO]
SFO = [ATL]
path=[ "ICN", "ATL", "ICN" ]

ICN = []
ATL = [SFO]
SFO = [ATL]
path=[ "ICN", "ATL", "ICN", "SFO" ]

ICN = []
ATL = [SFO]
SFO = []
path=[ "ICN", "ATL", "ICN", "SFO", "ATL" ]

ICN = []
ATL = []
SFO = []
path=[ "ICN", "ATL", "ICN", "SFO", "ATL", "SFO" ]
 */


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
    vector<string> result = { "ICN", "JFK", "HND", "IAD" };
	EXPECT_EQ(solution({ { "ICN", "JFK" }, { "HND", "IAD" }, { "JFK", "HND" } }), result);
}

TEST_F(CLASS_NAME, __LINE__)
{
    vector<string> result = { "ICN", "ATL", "ICN", "SFO", "ATL", "SFO" };
	EXPECT_EQ(solution({ { "ICN", "SFO" }, {"ICN", "ATL"}, { "SFO", "ATL" }, { "ATL", "ICN" }, { "ATL","SFO" } }), result);
}


int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
