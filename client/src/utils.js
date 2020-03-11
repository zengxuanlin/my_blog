/*
 * @Author: your name
 * @Date: 2020-03-11 16:52:14
 * @LastEditTime: 2020-03-11 16:57:18
 * @LastEditors: your name
 * @Description: In User Settings Edit
 * @FilePath: /client/src/utils.js
 */
function gmtToDate(gmt) {
    let date = new Date(gmt+'+0800')
    let Str = date.getFullYear() + '-' +
        (date.getMonth() + 1) + '-' +
        date.getDate() + ' ' +
        date.getHours() + ':' +
        date.getMinutes() + ':' +
        date.getSeconds()
    return Str
}

export {gmtToDate}