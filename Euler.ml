

(*let quicksortPart l p = 
       let base = ([],[]) in
       let fold_fn (l1,l2) elmt = 
              if elmt <= p then (elmt::l1; l2)
              else (l1, elmt::l2)
       in
       List.fold_left fold_fn base l
*)

let rec isPrime l n = match l with
        |[]->true
        |h::t -> 
                if n mod h = 0 then false
                (*else if h*h > n then true*)
                else isPrime t n

let rec euler7 l n m = 
        if List.length l = m then List.nth l 0 
        else 
                if (isPrime l n) then euler7  (n::l) (n+1)  m
                else euler7 l (n+1) m
                
let sumList l = 
        let base = 0 in
        let fold_fn acc elmt = (acc + elmt) in
        List.fold_left fold_fn base l

let rec euler8 l n = 
        if n = 2000000 then 
                sumList l 
        else
                if (isPrime l n) then euler8 (n::l) (n+1) (*l@[n]) (n+1*)
                else euler8 l (n+1) 






       
