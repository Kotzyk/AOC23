package helpers

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"time"
)

func ReadFileIntoArray(filePath string) []string {
	readFile, err := os.Open(filePath)
	defer func(readFile *os.File) {
		err = readFile.Close()
	}(readFile)
	if err != nil {
		fmt.Println(err)
	}
	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)
	var fileLines []string

	for fileScanner.Scan() {
		fileLines = append(fileLines, fileScanner.Text())
	}
	return fileLines
}

func TimeTrack(start time.Time, name string) {
	elapsed := time.Since(start)
	log.Printf("%s took %s", name, elapsed)
}
