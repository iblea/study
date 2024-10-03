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
    int solution(string name);
};

// 내가푼 답
#include <map>
int get_rtotal_skip(string name, int index);
int get_ltotal_skip(string name, int index);

int Solution::solution(string name) {
    map<char, int> alphabet = {
        {'A', 0},
        {'B', 1}, {'Z', 1},
        {'C', 2}, {'Y', 2},
        {'D', 3}, {'X', 3},
        {'E', 4}, {'W', 4},
        {'F', 5}, {'V', 5},
        {'G', 6}, {'U', 6},
        {'H', 7}, {'T', 7},
        {'I', 8}, {'S', 8},
        {'J', 9}, {'R', 9},
        {'K', 10}, {'Q', 10},
        {'L', 11}, {'P', 11},
        {'M', 12}, {'O', 12},
        {'N', 13},
    };

    int alphabet_cursor = 0;
    int cursor_move_left = 0;
    int cursor_move_right = 0;
    int skip = 1;
    int last_changed_index = 0;
    for (char c : name) {
        alphabet_cursor += alphabet[c];
    }
    for (int i = 1; i < name.size(); ++i) {
        if (name[i] == 'A') {
            skip++;
        } else {
            // ABAAAAAAAAAABAA
            int return_cursor_count = last_changed_index + (name.size() - i);
            int total_skip = skip + get_ltotal_skip(name, i);
            if (last_changed_index != 0 && return_cursor_count < total_skip) {
                // 되돌아가는 것이 더 빠르면 되돌아가야한다.
                cursor_move_left += return_cursor_count;
                break;
            }
            cursor_move_left += skip;
            skip = 1;
            last_changed_index = i;
        }
    }
    skip = 1;
    last_changed_index = 0;
    for (int i = name.size() - 1; i > 0; --i) {
        if (name[i] == 'A') {
            skip++;
        } else {
            int return_cursor_count = name.size() - last_changed_index + i;
            int total_skip = skip + get_rtotal_skip(name, i);
            if (last_changed_index != 0 && return_cursor_count < total_skip) {
                // 되돌아가는 것이 더 빠르면 되돌아가야한다.
                cursor_move_right += return_cursor_count;
                break;
            }
            cursor_move_right += skip;
            skip = 1;
            last_changed_index = i;
        }
    }
    // printf("CONSOLE | cursor_move_left : %d\n", cursor_move_left);
    // printf("CONSOLE | cursor_move_right : %d\n", cursor_move_right);
    // printf("CONSOLE | alphabet_cursor : %d\n", alphabet_cursor);

    if (cursor_move_left < cursor_move_right) {
        return cursor_move_left + alphabet_cursor;
    } else {
        return cursor_move_right + alphabet_cursor;
    }

    return 0;
};

int get_rtotal_skip(string name, int index) {
    int total_skip = 0;
    int tmp = 1;
    for (int j = index - 1; j > 0; --j) {
        if (name[j] == 'A') {
            tmp++;
        } else {
            total_skip += tmp;
            tmp = 1;
        }
    }
    return total_skip;
}

int get_ltotal_skip(string name, int index) {
    int total_skip = 0;
    int tmp = 1;
    for (int j = index + 1; j < name.size(); ++j) {
        if (name[j] == 'A') {
            tmp++;
        } else {
            total_skip += tmp;
            tmp = 1;
        }
    }
    return total_skip;
}


// 정답지
int solution1(string name) {
    int LUT[] = { 0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1 };
    int answer = 0;
    for (auto ch : name)
        answer += LUT[ch - 'A'];
    int len = name.length();
    int left_right = len - 1;
    for (int i = 0; i < len; ++i) {
        int next_i = i + 1;
        // BBBBAAAABA
        // i = 3
        // next_i = 8
        // len = 10
        // 3 + 10 - 8 + min(3, 10 - 8)
        // ABAAAABBBA
        // i = 1
        // next_i = 6
        // 1 + 10 - 6 + min(1, 10 - 6)
        while (next_i < len && name[next_i] == 'A')
            next_i++;
        left_right = min(left_right, i + len - next_i + min(i, len - next_i));
    }
    answer += left_right;
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
	EXPECT_EQ(this->s.solution("JAZ"), 11);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("JEROEN"), 56);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("JAN"), 23);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("AAA"), 0);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("AAAA"), 0);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("AABA"), 3);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("ABA"), 2);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("ABB"), 4);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("ABAAAAAAAAAABAA"), 7);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("AAAABAAAAAAAAAAABA"), 10);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("AABAAABAA"), 8);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("ABABAAAAABA"), 10);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("BBBBAAAABA"), 12);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("ABAAAABBBA"), 10);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("BABBAAAABA"), 11);
}

TEST_F(CLASS_NAME, __LINE__)
{
	EXPECT_EQ(this->s.solution("AABBAAAABA"), 10);
}



int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}