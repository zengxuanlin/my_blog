/*
 * @Author: your name
 * @Date: 2020-03-11 16:52:14
 * @LastEditTime: 2020-03-26 15:42:47
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /client/src/utils.js
 */
function gmtToDate(gmt) {
    let date = new Date(gmt+'+0800')
    let hh =  date.getHours() < 10?'0'+ date.getHours(): date.getHours();
    let mm =  date.getMinutes()<10?'0'+date.getMinutes():date.getMinutes();
    let ss = date.getSeconds()<10?'0'+date.getSeconds():date.getSeconds();
    let Str = date.getFullYear() + '-' +
        (date.getMonth() + 1) + '-' +
        date.getDate() + ' ' +
        hh + ':' +
        mm + ':' +
        ss
    return Str
}

export {gmtToDate}