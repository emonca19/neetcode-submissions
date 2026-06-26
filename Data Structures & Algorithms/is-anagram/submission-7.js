class Solution {
    
    isAnagram(s, t) {

     if(s.length != t.length) return false;

     const mapa = new Map();

     for(const char of s){
        mapa.set(char, (mapa.get(char) || 0)+1);
     }

     for(const char of t){
        if(!mapa.has(char)) return false;
        mapa.set(char, mapa.get(char)-1);
        if(mapa.get(char)< 0){
            return false;
        }

     }
     return true;

    }
}
