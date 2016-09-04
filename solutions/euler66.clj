
(defn take-until
  "Returns a lazy sequence of successive items from coll until
   (pred item) returns true, including that item. pred must be
   free of side-effects."
  [pred coll]
  (lazy-seq
    (when-let [s (seq coll)]
      (if (pred (first s))
        (cons (first s) nil)
        (cons (first s) (take-until pred (rest s)))))))


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


(defn convergent
  ([continueds]
   (convergent (rest continueds) (first continueds)))
  ([continueds value]
   (if (empty? continueds)
     value
     (+ value (/ 1 (convergent (rest continueds) (first continueds)))))))

(defn period [s]
  (let [generator (continued s)
        a0 (first generator)]
    (take-until (fn [x] (= (* a0 2) x)) (drop 1 generator))))

(defn period-length [s]
  (count (period s)))


(defn find-convergent-length [n]
  (let [r (period-length n)]
    (if (even? r)
      r
      (* 2 r))))

(defn find-x-and-y [n]
  (try
    (let [length (find-convergent-length n)
          conv (convergent (take length (map int (continued n))))
          x (if (ratio? conv) (numerator conv) conv)
          y (if (ratio? conv) (denominator conv) 1)]
      [x y])
    (catch Exception e [1 1])))


(->> (range 1000)
     (map (fn [D] [(find-x-and-y D) D]))
     (apply max-key ffirst)
     second)

