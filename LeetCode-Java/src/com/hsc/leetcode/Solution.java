package com.hsc.leetcode;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;


/**
 * @author shengchang
 * All the questions are solved here through imdependent methods
 *
 */
public class Solution {
	
    private static final int maxDiv10=Integer.MAX_VALUE/10;// a static value used for atoi
    List<Integer> list=new ArrayList<Integer>();//a field 
    
    
    
    public String shortestPalindrome(String s) {
        int sLength=s.length();
        int tail=0;
        while(tail<sLength){
            if( isaPalindrome( s.substring(0,sLength-tail) ) )
                break;
            tail++;
        }
        StringBuilder sb=new StringBuilder();
        
        for(int j=0;j<tail;j++)
        	sb.append(s.charAt(sLength-1-j));
        sb.append(s);
        return sb.toString();
        
    }
    
    
    private boolean isaPalindrome(String s){    //a private method used in shortestPalindrome
        int sLength=s.length();
        for(int i=0;i<sLength/2;i++){
            if(s.charAt(i)!=s.charAt(sLength-i-1) )
                return false;
        }
        return true;
    }
    
    
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
		if (nums1.length < nums2.length)
			return findMedianSortedArrays(nums2, nums1);// 保持nums2比较小
		boolean isEven = (nums1.length + nums2.length) % 2 == 0 ? true : false;
		
		if(nums2.length==0){
			if(isEven)
				return (double)(nums1[nums1.length/2]+nums1[nums1.length/2-1])/2;
			else 
				return nums1[nums1.length/2];
		}
		

		int head2 = 0, tail2 = nums2.length - 1;
		int half = (nums1.length + nums2.length) / 2;
		int mid1, mid2;

		while (tail2 >= head2) {
			mid2 = (tail2 + head2) / 2;
			mid1 = half - mid2;
			if (mid1 > 0 && nums1[mid1 - 1] > nums2[mid2]) {// mid1更小
				// head1 += (tail2 - head2) / 2;
				head2 = mid2 + 1;

			} else if (mid2 > 0 && nums1[mid1] < nums2[mid2 - 1]) {
				// tail1 -= (tail2 - head2) / 2;
				tail2 = mid2 - 1;
			} else {// 此时mid2为右侧第一个；

				if (isEven) {
					int n1, n2;
					if (mid2 > 0)
						n1 = Math.max(nums1[mid1 - 1], nums2[mid2 - 1]);
					else {
						n1 = nums1[mid1 - 1];
					}
					if (mid1 < nums1.length)
						n2 = Math.min(nums1[mid1], nums2[mid2]);
					else
						n2 = nums2[mid2];
					return (double) (n1 + n2) / 2;

				} else {
					return (double) Math.min(nums2[mid2], nums1[mid1]);
				}

			}
		}
		if (head2 >= nums2.length) {// 2全在左边
			if (isEven) {
				int n1;
				if(half-1-nums2.length<0)
					n1=nums2[nums2.length-1];
				else 
					n1 = Math.max(nums1[half - 1 - nums2.length],nums2[nums2.length-1]);
				
				int n2 = nums1[half - nums2.length];
				return (double) (n1 + n2) / 2;
			} else {
				return nums1[half - nums2.length];
			}

		} else if (tail2 < 0) { // nums2全在右边
			if (isEven) {
				int n1 = nums1[half - 1];
				
				int n2;
				if(half>=nums1.length)
					n2= nums2[0];
				else 
					n2=Math.min(nums1[half],nums2[0]);
				
				return (double) (n1 + n2) / 2;
			} else {
				return Math.min(nums1[half],nums2[0]);
			}

		}

		return 0;
    }
    
    
    public int lengthOfLongestSubstring(String s) {
    	Map<Character, Integer> charMap=new HashMap<>();
    	int maxLength=0,startpoint=0;
    	for(int i=0;i<s.length();i++){
    		if(charMap.containsKey(s.charAt(i))){
    			if(charMap.get(s.charAt(i))>=startpoint){
    				startpoint=charMap.get(s.charAt(i))+1;
    			}
    			charMap.put(s.charAt(i), i);
    		}
    		else {
				charMap.put(s.charAt(i), i);
			}
    		maxLength=Math.max(i-startpoint+1, maxLength);
    	}
    	return maxLength;
    }
    
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