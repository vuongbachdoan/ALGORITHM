function solution(N) {
    let temp = N.toString(2);
    let pattern = /10+(?=1)/g;
    let parts = temp.match(pattern);

    if (parts) {
        let longestPart = parts.reduce((a, b) => b.length > a.length ? b : a);
        return (longestPart.length - 1);
    } else {
        return 0;
    }
}