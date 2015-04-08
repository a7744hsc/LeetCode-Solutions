import java.util.ArrayList;
import java.util.List;


/**
 * @author shengchang
 * All the questions are solved here through imdependent methods
 *
 */
public class Solution {
	
    private static final int maxDiv10=Integer.MAX_VALUE/10;// a static value used for atoi
    List<Integer> list=new ArrayList<Integer>();//a field 
    
    
    
    
    
    
    /**
     * @author shengchang
     * @param root 要遍历的树的根节点
     * @return list 按前序遍历排列的表
     * @see 这段代码完成的并不漂亮，因为用到了一个实例变量，但是使用迭代的写法比较简洁。
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        if(root!=null){
            list.add(root.val);
            if(root.left!=null)preorderTraversal(root.left);
            if(root.right!=null)preorderTraversal(root.right);
        }
        return list;
        
    }
    
	/**
	 * @author shengchang
	 * @param str  一个任意字符串
	 * @return  当字符串满足条件返回得到的Integer值，否则返回0
	 * @see 这个代码是从 cleancode handbook 上得到的，并稍微加以改进。
	 * 		从这段代码中我主要得到以下几个知识点：
	 * 		1.Character.isWhitespace 和Character.getNumericValue
	 * 		2.在对数组curser或者String 的遍历锚点进行读取或者写入之前一定要确保没有越界
	 * 		3.变量的定义放在使用前。
	 */
	public int atoi(String str) {
		int curser=0,length=str.length();
		while(curser<length && Character.isWhitespace(str.charAt(curser)))
			curser++;
		int sign=1;
		if(curser<length&&str.charAt(curser)=='+')
			curser++;
		else if(curser<length&&str.charAt(curser)=='-'){
			sign=-1;curser++;
			
		}
		int num = 0,digit=0;
		while (curser<length&&Character.isDigit(str.charAt(curser))) {
			digit=Character.getNumericValue(str.charAt(curser));
			if(num>maxDiv10||num==maxDiv10&&digit>=8)
				return sign==1?Integer.MAX_VALUE:Integer.MIN_VALUE;
			num=num*10+digit;
			curser++;
		}
		return sign*num;
		
     
        
    }
	
	
	 public boolean isNumber(String s) {
	        s=s.trim();
	        if(Character.isLetter(s.charAt(s.length()-1))&&s.charAt(s.length()-1)!='e')
	        	return false;
	        try{
	        	Float.parseFloat(s);
	        	return true;
	        }
	        catch(NumberFormatException e){}
	        
	       return false;
	        
	    }
	
	
	
public String reverseWords(String s) {
	String[] temp=s.split(" +");
	StringBuilder sb=new StringBuilder();
	for(int i=temp.length-1;i>=0;i--){
			
				sb.append(temp[i]);
				if (i != 0) {
					sb.append(" ");
				}
			
	}
	
	return sb.toString().trim();        
    }
	
	public int strStr(String haystack, String needle) {
		
        for(int i=0;i<=haystack.length();i++){
            for(int j=0;j<=needle.length();j++){
                if(j==needle.length())
                    return i;
                if(i+j>=haystack.length())
                    return -1;
                if(haystack.charAt(i+j)!=needle.charAt(j)){
                    //yan'jiu'yi'dong'duo'shao'wei
                    //pipei  i+needle.length() he  needle(x)
                    int k=0;
                    while(k<needle.length()){
                        if(haystack.charAt(i+needle.length())!=needle.charAt(needle.length()-k-1))
                            k++;
                        else{
                            break;
                        }
                    }
                    i+=k;
                    break;
                }
                
            }
            
            
        }
		return 0;
        
    }

	public boolean isPalindrome(String s) {
		int cusorhead = 0, cusortail = s.length() - 1;
		while (cusorhead < cusortail) {
			while (!Character.isLetterOrDigit(s.charAt(cusorhead))
					&& cusorhead < s.length() - 1)
				cusorhead++;
			while (!Character.isLetterOrDigit(s.charAt(cusortail))
					&& cusortail > 0)
				cusortail--;
			if (Character.toLowerCase(s.charAt(cusorhead)) != Character
					.toLowerCase(s.charAt(cusortail)))
				return false;

			cusorhead++;
			cusortail--;
		}

		return true;

	}
}