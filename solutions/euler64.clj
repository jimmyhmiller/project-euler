(defn square [n]
  (* n n))

(defn square? [n]
  (let [s (Math/sqrt n)]
    (= (Math/floor s) s)))

(defn continued 
  ([s]
   (let [m0 0
         d0 1
         a0 (Math/floor (Math/sqrt s))

         generate (fn [[m d a]]
                    (let [m (- (* d a) m)
                          d (/ (- s (square m)) d)
                          a (Math/floor (/ (+ a0 m) d))]
                      [m d a]))]
     (map (fn [[_ _ a]] a) 
          (iterate generate [m0 d0 a0])))))




(defn period-length [s]
  (let [generator (continued s)
        a0 (first generator)]
    (count (take-while (fn [x] (not (= (* a0 2) x))) generator))))


(defn total-odd [n]
  (->> (range (inc n))
       (filter (complement square?))
       (map period-length)
       (filter odd?)
       count))


(print (total-odd 10000))
