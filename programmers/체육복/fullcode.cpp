#include <gtest/gtest.h>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


/*
 *
 */

class Solution {
public:
    int solution(int n, vector<int> lost, vector<int> reserve);
};

int Solution::solution(int n, vector<int> lost, vector<int> reserve) {
    for (auto it = lost.begin(); it != lost.end();) {
        auto found = find(reserve.begin(), reserve.end(), *it);
        if (found != reserve.end()) {
            reserve.erase(found);
            it = lost.erase(it);
        } else {
            ++it;
        }
    }

    // 정렬 안하면 반례 케이스가 존재함.
	// EXPECT_EQ(this->s.solution(5, {5, 3}, {4, 2}), 5);
    // 이 경우 4가 5를 제거하지 않고 3을 제거해버리며 2가 3을 제거할 수 없음.
    sort(reserve.begin(), reserve.end());

    for (int val : reserve) {
        auto found = find(lost.begin(), lost.end(), val - 1);
        if (found != lost.end()) {
            lost.erase(found);
            continue;
        }
        found = find(lost.begin(), lost.end(), val + 1);
        if (found != lost.end()) {
            lost.erase(found);
            continue;
        }
    }

    return n - lost.size();
}


#define CLASS_NAME gtest_template

class CLASS_NAME: public ::testing::Test {
private:
	clock_t t0;
	clock_t t1;
public:
	Solution s;
protected:
	CLASS_NAME() { this->s = Solution(); }
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
	EXPECT_EQ(this->s.solution(5, {2, 4}, {1, 3, 5}), 5);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {2, 4}, {3}), 4);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(3, {3}, {1}), 2);
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {3}, {3, 5}), 5);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {3}, {3}), 5);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {2, 4}, {3}), 4);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {2, 4, 5}, {3, 4}), 4);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {2}, {}), 4);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {}, {3}), 5);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {2, 3}, {3, 4}), 4);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {4, 2}, {3, 5}), 5);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution(5, {5, 3}, {4, 2}), 5);
}


int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}