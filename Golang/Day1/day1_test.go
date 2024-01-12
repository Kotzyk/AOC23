package tests

import (
	"github.com/Kotzyk/AOC2023/Day1"
	"testing"
)

func TestGetCalibrationValue(t *testing.T) {
	var tests = []struct {
		name  string
		input string
		want  int
	}{
		{"1abc2 gives 12", "1abc2", 12},
		{"pqr3stu8vwx gives 38", "pqr3stu8vwx", 38},
		{"a1b2c3d4e5f gives 15", "a1b2c3d4e5f", 15},
		{"treb7uchet gives 77", "treb7uchet", 77},
		{"two1nine gives 11", "two1nine", 11},
		{"abcone2threexyz gives 22", "abcone2threexyz", 22},
	}
	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			ans := Day1.GetCalibrationValue(tc.input, false)
			if ans != tc.want {
				t.Errorf("got %d, want %d", ans, tc.want)
			}
		})
	}
}
