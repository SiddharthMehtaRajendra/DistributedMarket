package turtledover

import java.sql.{Connection, DriverManager, ResultSet}
import org.postgresql.Driver

class DMJobsDB {
    var conn : Connection = null
    def connect() {
        val con_str = "jdbc:postgresql://db:5432/postgres"
        conn = DriverManager.getConnection(con_str, "postgres", "123456")
    }

    def close() {
        if(conn != null) {
            conn.close()
            conn = null
        }
    }

    def update_status(jobId: String, status: String) : Boolean = {
        if(conn == null) {
            println("No connection")
            return false
        }

        try {
            val stm = conn.prepareStatement("UPDATE services_job set status=? WHERE job_id=?")
            stm.setString(1, status)
            stm.setInt(2, jobId.toInt)
            val result = stm.executeUpdate()
            println("Update affect " + result + " rows.")
        } catch {
            case e: Exception => {
                println("execute update fail, message=" + e.getMessage)
            }
        }
        return true
    }

    def update_spark_id(jobId: String, sparkId: String) : Boolean = {
        if(conn == null) {
            println("No connection")
            return false
        }

        try {
            val stm = conn.prepareStatement("UPDATE services_job set spark_id=? WHERE job_id=?")
            stm.setString(1, sparkId)
            stm.setInt(2, jobId.toInt)
            val result = stm.executeUpdate()
            println("Update affect " + result + " rows.")
        } catch {
            case e: Exception => {
                println("execute update fail, message=" + e.getMessage)
            }
        }
        return true
    }
}
