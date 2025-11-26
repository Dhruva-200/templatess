print("hello world yea how your day going mate well it is a wednesdayand we have ooout lab internals so lets see what happens ")
'''
package com.cicd.demo;
import java.io.FileReader;
import java.io.IOException;
public class retrivefile {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 String filePath = "src/main/resources/data.json";

	        try (FileReader reader = new FileReader(".\\JSON\\test.json")) {
	            int ch;
	            while ((ch = reader.read()) != -1 ) {
	            	
	                System.out.print((char) ch);
	            }
	        } catch (IOException e) {
	            e.printStackTrace();
	        }
	}

}
'''