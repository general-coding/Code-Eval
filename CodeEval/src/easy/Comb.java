import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;
import java.util.TreeSet;


public class Comb {
	TreeSet hs = new TreeSet();	
	public TreeSet permutation(String prefix, String str) {
        int n = str.length();
        if (n == 0)
        {
        	hs.add(prefix);
        	//System.out.println(prefix);
        }
        else
        {
        	hs.add(prefix);
            //System.out.println(prefix);
        }
            for(int i = 0;i < n;i++)
                permutation(prefix+str.charAt(i), str.substring(0, i)+str.substring(i+1, n));
            return hs;
        
    }
	void print (TreeSet hs)
	{
		Iterator itr = hs.iterator();
		while(itr.hasNext())
		{
			String str = (String)itr.next();
            System.out.println(str);
		}
	}


	public static void main(String[] args) {
		Comb b = new Comb();
		String ss = "abc";
		TreeSet hss = b.permutation("", ss);
		System.out.println("Printing in acsending order....................");

		b.print(hss);
		int i;
		ArrayList al = new ArrayList();
		for (i = 1;i<=ss.length() ; i++)	
		{
			Iterator itr = hss.iterator();
			while(itr.hasNext())
			{
				String str = (String)itr.next();
				if(str.length()==i)
				{
					al.add(str);
				}
			}	
		}
		System.out.println("Printing in acsending order and ascending length....................");
		for (i=0;i<al.size(); i++)
		{
			System.out.println((String)al.get(i));
		}
	}
}
