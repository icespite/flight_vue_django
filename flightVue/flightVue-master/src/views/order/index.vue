<template>
  <div>
    <div class="app-container">
      <el-button>Done</el-button>
      <el-table
        v-loading="listLoading"
        :data="donelist"
        element-loading-text="Loading"
        border
        fit
        highlight-current-row
      >
        <el-table-column align="center" label="ID" width="95">
          <template slot-scope="scope">
            {{ scope.$index+1 }}
          </template>
        </el-table-column>
        <el-table-column label="flightNumber">
          <template slot-scope="scope">
            {{ scope.row.flightNumber }}
          </template>
        </el-table-column>
        <el-table-column label="time" align="center">
          <template slot-scope="scope">
            <i class="el-icon-time" />
            <span>{{ scope.row.time }}</span>
          </template>
        </el-table-column>
        <el-table-column label="seat" align="center">
          <template slot-scope="scope">
            {{ scope.row.seat }}
          </template>
        </el-table-column>
        <el-table-column class-name="status-col" label="Status" align="center">
          <template slot-scope="scope">
            <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status| msgFilter }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="operate" align="center">
          <template slot-scope="scope">
            <el-button  @click="cancelBuy(scope.row.id,'done')">退票</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="app-container">
      <el-button>Wait</el-button>
      <el-table
        v-loading="listLoading"
        :data="waitlist"
        element-loading-text="Loading"
        border
        fit
        highlight-current-row
      >
        <el-table-column align="center" label="ID" width="95">
          <template slot-scope="scope">
            {{ scope.$index+1 }}
          </template>
        </el-table-column>
        <el-table-column label="flightNumber">
          <template slot-scope="scope">
            {{ scope.row.flightNumber }}
          </template>
        </el-table-column>
        <el-table-column label="time" align="center">
          <template slot-scope="scope">
            <i class="el-icon-time" />
            <span>{{ scope.row.time }}</span>
          </template>
        </el-table-column>
        <el-table-column label="seat" align="center">
          <template slot-scope="scope">
            {{ scope.row.seat }}
          </template>
        </el-table-column>
        <el-table-column class-name="status-col" label="Status" align="center">
          <template slot-scope="scope">
            <el-tag :type="scope.row.status | statusFilter">{{ scope.row.status| msgFilter }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="operate" align="center">
          <template slot-scope="scope">
            <el-button  @click="cancelBuy(scope.row.id,'wait')">退票</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import { getbuyinfo, cancelbuy } from '../../api/user'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        1: 'primary',
        2: 'info',
        0: 'danger'
      }
      return statusMap[status]
    },
    msgFilter(status) {
      const statusMap = {
        1: 'normal',
        2: 'delay',
        0: 'cancel'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      donelist: null,
      waitlist: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getbuyinfo().then(response => {
        this.donelist = response.data.done
        this.waitlist = response.data.wait
        this.listLoading = false
      })
    },
    open(title = '标题', msg = '提示') {
      this.$notify({
        title: title,
        message: msg,
        type: 'success'
      })
    },
    cancelBuy(id, classify) {
      cancelbuy(id, classify).then(
        response => {
          if (response.code === 20000) {
            this.open('success', '更新成功')
          }
          this.fetchData()
        }

      )
    }
  }
}
</script>
