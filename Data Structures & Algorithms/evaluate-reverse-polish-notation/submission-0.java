class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> ops = new Stack<>();
        HashSet<String> a = new HashSet<>();
        a.add("+");
        a.add("-");
        a.add("*");
        a.add("/");

        for(String s : tokens){
            if(!a.contains(s)){
                ops.add(s);
                continue;
            }
            int first = Integer.valueOf(ops.pop());
            int second = Integer.valueOf(ops.pop());
            if(s.equals("+")){
               ops.add(String.valueOf(second + first));
            }else if(s.equals("-")){
               ops.add(String.valueOf(second - first));
            }else if(s.equals("*")){
               ops.add(String.valueOf(second * first));
            }else if(s.equals("/")){
               ops.add(String.valueOf(second / first));
            }
            // System.out.println("here " + ops);

        }
        System.out.println(ops);
        return Integer.parseInt(ops.peek());
    }
}
