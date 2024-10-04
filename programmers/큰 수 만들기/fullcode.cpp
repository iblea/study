#include <gtest/gtest.h>
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;


/*
 *
 */

class Solution {
public:
    string solution();
};

string Solution::solution() { return "template_function"; };

string solution(string number, int k) {
    int len = number.length();
    int remain = len - k;

    string answer = "";
    int ans_len = 0;
    for (int i = len - 1; i >= 0; --i) {
        if (ans_len < remain) {
            answer = number[i] + answer;
            ans_len++;
            continue;
        }

        // 제거
        if (answer[0] > number[i]) {
            // 앞자리수가 더 작으면 skip
            // ex ) answer = 791, number[i] = 5 -> 5791 이면 5를 추가할 필요가 없다.
            continue;
        }
        // 7861 -> 786
        // 7816 -> 786
        // 7691 -> 791
        int j = 0;
        for (j = 0; j < ans_len - 1; ++j) {
            if (answer[j] >= answer[j+1]) {
                continue;
            }
            answer = answer.substr(0, j) + answer.substr(j + 1);
            break;
        }
        if (j == ans_len - 1) {
            answer = answer.substr(0, j);
        }
        answer = number[i] + answer;
    }
    return answer;
}

string solution_answer(string number, int k) {
    string answer = "";
    answer = number.substr(k);
    for(int i = k-1;i >=0;i--){
        int j = 0;
        do{
            if(number[i] >= answer[j]){
                char temp = answer[j];
                answer[j] = number[i];
                number[i] = temp;
                j++;
            }else{
                break;
            }
        }while(1);
    }

    return answer;
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
	EXPECT_EQ(solution("1924", 2), "94");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("1231234", 3), "3234");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("4177252841", 4), "775841");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("12345", 2), "345");
}
TEST_F(CLASS_NAME, __LINE__)
{
    string res = solution("54321", 2);
    cout << "result: " << res << endl;
	EXPECT_EQ(solution("54321", 2), "543");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("51234", 2), "534");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("54123", 2), "543");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("57213", 2), "723");
    // 3
    // 13
    // 213
    // 7213 -> 723
    // 5723 -> 723
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("57219", 2), "729");
    // 9
    // 19
    // 219
    // 7219 -> 729
    // 5729 -> 729
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("57291", 2), "791");
    // 1
    // 91
    // 291
    // 7291 -> 791
    // 5791 -> 791
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("57991", 2), "991");
    // 1
    // 91
    // 991
    // 7991 -> 991
    // 5991 -> 991
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("57681", 2), "781");

    // 1
    // 81
    // 681
    // 7681 -> 768
    // 57681 -> 768
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("8888", 1), "888");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("8887", 1), "888");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("7888", 1), "888");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("7888", 3), "8");
}
TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(solution("888", 2), "8");
}




int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}