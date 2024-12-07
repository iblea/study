#include <gtest/gtest.h>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

/*
n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

제한사항

섬의 개수 n은 1 이상 100 이하입니다.
costs의 길이는 ((n-1) * n) / 2이하입니다.
임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
연결할 수 없는 섬은 주어지지 않습니다.
*/

int solution(int n, vector<vector<int>> costs) {
    int answer = 0;

    // 크루스칼 알고리즘 사용 필요
    // 3번째 인덱스에 비용이 들어가 있음 3번째 인덱스를 기준으로 오름차순 정렬
    sort(costs.begin(), costs.end(), [](vector<int> a, vector<int> b) {
        return a[2] < b[2];
    });

    // 부모 노드를 저장할 배열
    vector<int> parent(n);

    // union-find 알고리즘 사용
    for (int i = 0; i < n; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < costs.size(); i++) {
        int start = costs[i][0];
        int end = costs[i][1];
        int cost = costs[i][2];

        // 사이클이 발생하지 않는 경우
        if (parent[start] != parent[end]) {
            if (parent[start] > parent[end]) {
                swap(start, end);
            }
            // 두 노드의 부모 노드를 찾아서 작은 값으로 설정
            int min_parent = parent[start];
            int max_parent = parent[end];

            // max_parent 값인 부모 노드의 값 조정
            for (int j = 0; j < n; j++) {
                if (parent[j] == max_parent) {
                    parent[j] = min_parent;
                }
            }

            answer += cost;
        }
        // 사이클이 발생하는 경우는 스킵한다. (어차피 비용이 더 크기 때문에)
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
    EXPECT_EQ(solution(4, { { 0,1,1 },{ 0,2,2 },{ 1,2,5 },{ 1,3,1 },{ 2,3,8 } }), 4);
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
