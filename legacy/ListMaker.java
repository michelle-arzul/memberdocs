 // Created by Michelle Arzul (c) 2012

/* Search for "!" for context instructions.
 * Once all changes have been made, click the "Build File" button above (in JCreator, the blue down arrow) to compile the code.
 * Then click the "Run Project" button above (in JCreator, the blue play arrow) to run the List Maker.
 * CAUTION! The file ListMaker.java MUST be in the same folder as the images and csv file.
 */

import java.util.Scanner;
import java.io.*;

public class ListMaker {
	public static void main(String[] args) throws IOException{
		
		/* ! - Put desired name of output html file in the double quotes of the first line below this comment.
		 * For example: PrintWriter out = new PrintWriter(new FileWriter("8A.html"));
		 * Remember the extention, file name not case sensitive.
		 */
		
		PrintWriter out = new PrintWriter(new FileWriter("8A.html"));
		
		out.println("<html><head><title></title></head><body><table>");
				
		/* ! - Put name of csv file to be read in the double quotes of the first line below this comment.
		 * For example: Scanner in = new Scanner(new File("8a.csv"));
		 * Remember the extension, not case sensitive.
		 */
		
		Scanner in = new Scanner(new File("grade 8A.csv"));
		
		int num = 0;
		
		while(in.hasNext()){
			
			Scanner[] line = new Scanner[4];
			int cells = 0;
			
			if(in.hasNext()){
				line[0] = new Scanner(in.nextLine());
				cells = 1;
			}
			if(in.hasNext()){
				line[1] = new Scanner(in.nextLine());
				cells = 2;
			}
			if(in.hasNext()){
				line[2] = new Scanner(in.nextLine());
				cells = 3;
			}
			if(in.hasNext()){
				line[3] = new Scanner(in.nextLine());
				cells = 4;
			}
			
			switch(cells){
				case 1:{
					line[0].useDelimiter(",");
					break;
				}
				case 2:{
					line[1].useDelimiter(",");
					line[0].useDelimiter(",");
					break;
				}
				case 3:{
					line[2].useDelimiter(",");
					line[1].useDelimiter(",");
					line[0].useDelimiter(",");
					break;
				}
				case 4:{
					line[3].useDelimiter(",");
					line[2].useDelimiter(",");
					line[1].useDelimiter(",");
					line[0].useDelimiter(",");
					break;
				}
			}
			
			out.println("<tr>");
			for(int i = 0; i < cells; i++){
			//	num = Integer.parseInt(line[i].next());
				String numS = line[i].next();
			//	if(num<10)
			//		numS = "0"+num;
			//		else numS = ""+num;
				out.println("<td>");
				out.println("<img src=\""+numS+".jpg\" width=133 height=177 align=center>");
				out.println("</td>");
			}
			out.println("</tr><tr>");
			for(int i = 0; i < cells; i++){
				out.println("<td><div align=\"center\">");
				out.println(line[i].next().toUpperCase()+"<br>"+line[i].next().toUpperCase());
				out.println("</div></td>");
			}
			out.println("</tr>");
		}
		out.println("</table></body></html>");
		out.close();
	}
}
// ! - End of instructions.