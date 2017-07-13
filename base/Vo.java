package com.cdsq.manage.base;

/**
 * 项目名称：车到山前后台
 * 类描述：
 * 创建人：yzh
 * 创建时间：2017年06月01日
 * 备注：
 */
public class Vo {
    private Integer pageNumber = 1; // 当前页
    private Integer pageSize = 10; // 每页数量

    private Integer pageIndex;  // 当前页起始位置

    public Integer getPageNumber() {
        return pageNumber;
    }

    public void setPageNumber(Integer pageNumber) {
        this.pageNumber = pageNumber;
    }

    public Integer getPageSize() {
        return pageSize;
    }

    public void setPageSize(Integer pageSize) {
        this.pageSize = pageSize;
    }

    public Integer getPageIndex() {
        return pageNumber * pageSize - pageSize;
    }

    public void setPageIndex(Integer pageIndex) {
        this.pageIndex = pageIndex;
    }
}
